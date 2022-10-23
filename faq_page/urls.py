from django.urls import path
from faq_page.views import show_faqpage
from .views import create_disc, del_post, del_rep, edit_post, forum, add_reply

app_name = 'wishlist'

urlpatterns = [
    path('', show_faqpage, name='show_faqpage'),
]