from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class WorkbookViewAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='example@example.com',
            password='test456', is_email_confirmed=True)

    def test_create_workbook(self):
        url = reverse('workbook:workbook-list')
        data = {'name': 'workbook name'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.user.workbooks.count(), 1)

    def test_create_workbook_unauthenticated(self):
        url = reverse('workbook:workbook-list')
        data = {'name': 'workbook name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(self.user.workbooks.count(), 0)

    def test_create_workbook_unverified(self):
        self.user.is_email_confirmed = False
        self.user.save()
        url = reverse('workbook:workbook-list')
        data = {'name': 'workbook name'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.user.workbooks.count(), 0)


