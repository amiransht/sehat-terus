from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse, resolve
from about.views import show_about

class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'about:show_about'
        )
      

    def test_url1_exist(self):
        self.assertEqual(
            resolve(self.urlToViewHtml).func,show_about
        )
