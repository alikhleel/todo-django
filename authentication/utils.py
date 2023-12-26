from django.core.mail import send_mail
from django.template.loader import get_template
from django.urls import reverse

import authentication


def send_confirmation_email(email,  redirect_url):
    data = {
        'redirect_url': redirect_url
    }
    message = f"{get_template('confirmation_email.txt').render(data)}"
    send_mail(
        subject='Please Confirm email',
        message=message,
        from_email='admin@admin.com',
        recipient_list=[email],
        fail_silently=False,
    )
