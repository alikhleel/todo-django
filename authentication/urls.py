from django.urls import path
from rest_framework.authtoken.views import (obtain_auth_token)

from authentication.views import SignupView, UserInformationView, SendEmailConfirmationTokenView, LogoutView, \
    confirm_email

app_name = 'authentication'
urlpatterns = [
    path('login/', obtain_auth_token, name='login_api_view'),
    path('logout/', LogoutView.as_view(), name='logout_api_view'),
    path('signup/', SignupView.as_view(), name='signup_api_view'),
    path('me/', UserInformationView.as_view(), name='user_information_api_view'),
    path('send-conformation-email/', SendEmailConfirmationTokenView.as_view(), name='send_conformation_email_api_view'),
    path('confirm-email/', confirm_email, name='confirm_email_api_view'),

]
