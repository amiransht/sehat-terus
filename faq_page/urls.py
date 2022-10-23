from django.urls import path
from faq_page.views import show_faqpage

app_name = 'faq_page'

urlpatterns = [
    path('', show_faqpage, name='show_faqpage'),
]