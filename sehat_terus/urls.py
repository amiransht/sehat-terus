from django.urls import path
from sehat_terus.views import show_homepage, show_lurah_page

app_name = 'wishlist'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('lurah-page/', show_lurah_page, name='show_lurah_page'),
]