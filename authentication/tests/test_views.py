from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from authentication.models import EmailConfirmationToken

User = get_user_model()


class UsersAPIViewTests(APITestCase):
    def test_signup_api_view_is_working(self):
        url = reverse('authentication:signup_api_view')
        body = {
            'email': 'example@example.com',
            'password': 'test456',
        }
        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, 201)
        user = User.objects.filter(email=body['email']).first()
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password(body['password']))

    def test_signup_view_not_accepting_duplicate_email(self):
        user = User.objects.create_user(email='example@example.com', password='test456')
        url = reverse('authentication:signup_api_view')
        body = {
            'email': 'example@example.com',
            'password': 'test456',
        }
        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, 400)

    def test_user_information_api_view_requires_authentication(self):
        url = reverse('authentication:user_information_api_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_send_conformation_email_api_view_requires_authentication(self):
        url = reverse('authentication:send_conformation_email_api_view')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 401)

    def test_send_conformation_email_api_view_create_token(self):
        user = User.objects.create_user(email="example@example.com", password="test456")
        url = reverse('authentication:send_conformation_email_api_view')
        self.client.force_authenticate(user=user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 201)
        token = EmailConfirmationToken.objects.filter(user=user).first()
        self.assertIsNotNone(token)
