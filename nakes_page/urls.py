from django.urls import path
from nakes_page.views import show_nakes_page, show_json

app_name = 'nakes_page'

urlpatterns = [
    path('', show_nakes_page, name='show_nakes_page'),
    path('json/', show_json, name='show_json'),
]