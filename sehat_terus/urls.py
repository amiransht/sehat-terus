from django.urls import path
from sehat_terus.views import show_homepage

app_name = 'wishlist'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
]