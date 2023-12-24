from django.core.mail import send_mail
from django.template.loader import get_template


def send_confirmation_email(email, token_id, user_id):
    data = {
        'token_id': str(token_id),
        'user_id': str(user_id),
    }
    message = f"{get_template('confirmation_email.txt').render(data)}"
    send_mail(
        subject='Please Confirm email',
        message=message,
        from_email='admin@admin.com',
        recipient_list=[email],
        fail_silently=False,
    )
