from django.urls import path
from homepage.views import show_homepage, get_covid_api, show_json_pasien, show_json_pasien_id

app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('api-indonesia/', get_covid_api, name='covid-api'),
    path('json', show_json_pasien, name="show_json"),
    path('json/<int:id>', show_json_pasien_id, name="show_json"),



]