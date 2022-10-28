from django.urls import path
from faq_page.views import show_faqpage, tulis_blog, submit_blog, blog, getblog


app_name = 'faq_page'

urlpatterns = [
    path('', show_faqpage, name='show_faqpage'),
    path('tulis_blog', tulis_blog, name='tulis_blog'),
    path('submit_blog', submit_blog, name='submit_blog'),
    path('blog', blog, name='blog'),
    path('getblog', getblog, name='getblog')
]