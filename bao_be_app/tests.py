from django.test import TestCase

# Create your tests here.

# myapp/tests.py
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class YourAppTests(TestCase):
    def setUp(self):
        # Create a test user and set the secret key
        self.user = User.objects.create(username='testuser')
        self.secret_key = 'ghiblikey'

    def test_authenticated_api_call(self):
        client = APIClient()

        # Make an authenticated API call
        response = client.get('/api/get_all_films/', HTTP_AUTHORIZATION=self.secret_key)

        # Check if the response is successful (HTTP 200 OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more assertions based on the expected response content

    def test_unauthenticated_api_call(self):
        client = APIClient()

        # Make an unauthenticated API call without the Authorization header
        response = client.get('/api/get_all_films/')

        # Check if the response indicates unauthorized access (HTTP 401 Unauthorized)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Add more assertions based on the expected response content

    def test_invalid_secret_key(self):
        client = APIClient()

        # Make an API call with an invalid secret key
        response = client.get('/api/get_all_films/', HTTP_AUTHORIZATION='invalid_secret_key')

        # Check if the response indicates unauthorized access (HTTP 401 Unauthorized)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Add more assertions based on the expected response content

    # Add more test cases as needed
