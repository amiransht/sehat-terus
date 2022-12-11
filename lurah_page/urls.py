from django.urls import path
from lurah_page.views import add_pasien_ajax, show_lurah_homepage, show_lurah_page, delete_pasien, show_json, add_pasien_ajax, add_flutter

app_name = 'lurah_page'

urlpatterns = [
    path('pasien/', show_lurah_page, name='show_lurah_page'),
    path('json/', show_json, name='show_json'),
    path('pasien/add/', add_pasien_ajax, name='add_pasien_ajax'),
    path('pasien/delete-pasien/<int:id>/', delete_pasien, name='delete_pasien'),
    path('', show_lurah_homepage, name='show_lurah_homepage'),
    path('add-flutter/', add_flutter, name='add_flutter')
]
