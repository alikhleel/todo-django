from django.urls import path
from rest_framework.authtoken.views import (obtain_auth_token)

from authentication.views import SignupView, UserInformationView, SendEmailConfirmationTokenView, LogoutView, \
    confirm_email

app_name = 'authentication'

urlpatterns = [
    path('auth/login/', obtain_auth_token, name='login_api_view'),
    path('auth/logout/', LogoutView.as_view(), name='logout_api_view'),
    path('auth/signup/', SignupView.as_view(), name='signup_api_view'),
    path('auth/me/', UserInformationView.as_view(), name='user_information_api_view'),
    path('auth/send-conformation-email/', SendEmailConfirmationTokenView.as_view(),
         name='send_conformation_email_api_view'),
    path('auth/confirm-email/', confirm_email, name='confirm_email_api_view'),

]
