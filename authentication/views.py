from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from authentication.serializers import SignupSerializer
from .models import EmailConfirmationToken
from .utils import send_confirmation_email


class SignupView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer


class UserInformationView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        email = user.email
        is_email_confirmed = user.is_email_confirmed
        payload = {
            'email': email,
            'is_email_confirmed': is_email_confirmed,
        }
        return Response(payload, status=200)


class SendEmailConfirmationTokenView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        token = EmailConfirmationToken.objects.create(user=user)
        send_confirmation_email(user.email, token.pk, user.pk)
        return Response(data=None, status=201)


@api_view(['GET'])
def confirm_email(request):
    token_id = request.GET.get('token_id')
    user_id = request.GET.get('user_id')
    try:
        token = EmailConfirmationToken.objects.get(pk=token_id)
        user = token.user
        user.is_email_confirmed = True
        user.save()
        EmailConfirmationToken.objects.filter(user=user).delete()
        data = {'is_email_confirmed': True}
        return Response(data=data, status=200)
    except EmailConfirmationToken.DoesNotExist:
        data = {'is_email_confirmed': False}
        return Response(data=data, status=400)


class LogoutView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(data=None, status=204)
