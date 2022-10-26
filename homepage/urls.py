from django.urls import path
from homepage.views import show_homepage, get_covid_api, search_prov

app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('api-indonesia/', get_covid_api, name='covid-api'),
    path('search-provinsi/', search_prov, name='search-provinsi')


]