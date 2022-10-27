from django.urls import path
from lurah_page.views import add_pasien_ajax, show_lurah_page, add_pasien, delete_pasien, show_json, add_pasien_ajax

app_name = 'lurah_page'

urlpatterns = [
    path('', show_lurah_page, name='show_lurah_page'),
    path('json/', show_json, name='show_json'),
    path('add/', add_pasien_ajax, name='add_pasien_ajax'),
    path('delete-pasien/<id>/', delete_pasien, name='delete_pasien'),
]
