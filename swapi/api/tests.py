from django.test import TestCase
from django.test import Client

from unittest.mock import Mock, patch
from rest_framework.test import APITestCase
from rest_framework import status


from api import views

# class YourTests(APITestCase):

#     def test_get_films_success(self):
#         with patch('api.views.requests') as mock_requests:
#             mock_requests.get.return_value = mock_response = Mock()
#             mock_response.status_code = 200
#             mock_response.json.return_value = {'message': "Your expected response"}
#             # response = self.client.get(f'{'api/films'}')
#             response = self.client.get('/api/films/')    
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertIn(response.data, 'results')

#     def test_get_species_success(self):
#         with patch('api.views.requests') as mock_requests:
#             mock_requests.get.return_value = mock_response = Mock()
#             mock_response.status_code = 200
#             mock_response.json.return_value = {'message': "Your expected response"}
#             # response = self.client.get(f'{'api/films'}')
#             response = self.client.get('/api/species/')    
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
