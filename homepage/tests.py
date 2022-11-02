from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse, resolve
from homepage.views import show_homepage, show_json_pasien, get_covid_api

class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'homepage:show_homepage'
        )
        self.urlToViewJson = reverse(
            'homepage:show_json'
        )
        self.fetchApi = reverse(
            'homepage:covid-api'
        )

    def test_url1_exist(self):
        self.assertEqual(
            resolve(self.urlToViewHtml).func,show_homepage
        )
    def test_url2_exist(self):
        self.assertEqual(
            resolve(self.urlToViewJson).func,show_json_pasien
        )
    def test_url3_exist(self):
        self.assertEqual(
            resolve(self.fetchApi).func,get_covid_api
        )
