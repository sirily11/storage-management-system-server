from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class TestGetItems(APITestCase):
    def test_get_item(self):
        url = reverse()
