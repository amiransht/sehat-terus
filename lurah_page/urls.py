from django.urls import path
from lurah_page.views import show_lurah_page

app_name = 'lurah_page'

urlpatterns = [
    path('', show_lurah_page, name='show_lurah_page'),
]