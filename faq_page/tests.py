from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse, resolve
from faq_page.views import show_faqpage, tulis_blog, submit_blog, blog, getblog

class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'faq_page:show_faqpage'
        )
        self.urlToViewJson = reverse(
            'faq_page:getblog'
        )
        self.tulisblog = reverse(
            'faq_page:tulis_blog'
        )
        self.blog = reverse(
            'faq_page:blog'
        )
        self.submit_blog = reverse(
            'faq_page:submit_blog'
        )

    def test_url1_exist(self):
        self.assertEqual(
            resolve(self.urlToViewHtml).func,show_faqpage
        )
    def test_url2_exist(self):
        self.assertEqual(
            resolve(self.urlToViewJson).func,getblog
        )
    def test_url3_exist(self):
        self.assertEqual(
            resolve(self.tulisblog).func,tulis_blog
        )
    def test_url4_exist(self):
        self.assertEqual(
            resolve(self.submit_blog).func,submit_blog
        )
    def test_url5_exist(self):
        self.assertEqual(
            resolve(self.blog).func,blog
        )