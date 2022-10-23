from django.urls import path
from homepage.views import show_homepage

app_name = 'wishlist'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
]