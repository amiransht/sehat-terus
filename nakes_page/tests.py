from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse, resolve
from nakes_page.views import show_nakes_page, show_json

urlpatterns = [
    path('pasien/', show_nakes_page, name='show_nakes_page'),
    path('json/', show_json, name='show_json'),
    path('pasien/update/<int:id>', update_status_pasien, name='update'),
    path('', show_nakes_homepage, name='show_nakes_homepage'),
]
class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'nakes_page:show_nakes_page'
        )
        self.urlToViewJson = reverse(
            'nakes_page:show_json'
        )
        self.nakes = reverse(
            'nakes_page:show_nakes_homepage'
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
            resolve(self.pasien).func,show_nakes_page
        )