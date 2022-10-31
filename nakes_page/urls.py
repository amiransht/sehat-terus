from django.urls import path
from nakes_page.views import show_nakes_page, show_json, update_status_pasien

app_name = 'nakes_page'

urlpatterns = [
    path('', show_nakes_page, name='show_nakes_page'),
    path('json/', show_json, name='show_json'),
    path('update/<int:id>', update_status_pasien, name='update'),
]