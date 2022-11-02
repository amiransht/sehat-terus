from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse, resolve
from lurah_page.views import show_lurah_homepage, show_lurah_page, show_json, add_pasien_ajax

class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'lurah_page:show_lurah_homepage'
        )
        self.urlToViewJson = reverse(
            'lurah_page:show_json'
        )
        self.add = reverse(
            'lurah_page:add_pasien_ajax'
        )
        self.pasien = reverse(
            'lurah_page:show_lurah_page'
        )

    def test_url1_exist(self):
        self.assertEqual(
            resolve(self.urlToViewHtml).func,show_lurah_homepage
        )
    def test_url2_exist(self):
        self.assertEqual(
            resolve(self.urlToViewJson).func,show_json
        )
    def test_url3_exist(self):
        self.assertEqual(
            resolve(self.add).func,add_pasien_ajax
        )
    def test_url5_exist(self):
        self.assertEqual(
            resolve(self.pasien).func,show_lurah_page
        )