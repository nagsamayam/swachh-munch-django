from rest_framework.test import APIClient
#from django.urls import reverse
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from swachh_munch.factories import Channel as ChanelFactories
from basic.models import Channel
from rest_framework import status

User = get_user_model()


class ProfileCreateViewTest(APITestCase):

    def setUp(self):
        channels = Channel.objects.all()
        if not channels.exists():
            ChanelFactories.ChannelFactory.create()
        self.test_user = User.objects.create_user('admin', 'nag.samayam@gmail.com', '12345678')
        self.create_url = reverse('api-profiles:account-create')
        self.data = {
            'username': 'samayam',
            'email': 'samayam.nag@gmail.com',
            'password': '12345678',
        }
    
    def test_user_can_create_account(self):
        data = {
            'username': 'samayam',
            'email': 'samayam.nag@gmail.com',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)


    def test_username_should_not_be_empty(self):
        data = {
            'username': '',
            'email': 'samayam.nag@gmail.com',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['username']), 1)


    def test_username_should_be_unique(self):
        data = {
            'username': 'admin',
            'email': 'samaya.nag@gmail.com',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['username']), 1)

    def test_username_should_have_min_length(self):
        data = {
            'username': 'ad',
            'email': 'samaya.nag@gmail.com',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['username']), 1)

    def test_username_should_not_exceed_max_length(self):
        data = {
            'username': 'admin'*10,
            'email': 'samaya.nag@gmail.com',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['username']), 1)

    def test_email_shold_not_be_empty(self):
        data = {
            'username': 'samayam',
            'email': '',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['email']), 1)

    def test_email_shold_be_valid_one(self):
        data = {
            'username': 'samayam',
            'email': 'samaya.nag',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['email']), 1)

    def test_email_shold_be_unique(self):
        data = {
            'username': 'samayam',
            'email': 'nag.samayam@gmail.com',
            'password': '12345678',
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['email']), 1)
    
    def test_password_shold_not_be_empty(self):
        self.data['password'] = ''

        response = self.client.post(self.create_url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['password']), 1)

    def test_password_shold_have_min_length(self):
        self.data['password'] = '12345'

        response = self.client.post(self.create_url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(len(response.data['password']), 1)

    def test_user_can_login_with_email(self):

        response = self.client.post('/api-token-auth/', {'username': self.test_user.email, 'password': "12345678"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['token'])

    def test_user_should_be_unauthenticated_on_invalid_credentials(self):
        response = self.client.post('/api-token-auth/', {'username': self.test_user.username, 'password': "1234"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


