from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

class PermissionsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass"
        )

    def test_unauthorized_access(self):
        response = self.client.get("/api/furniture/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/furniture/")
        self.assertNotEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
