from django.urls import path
from homepage.views import show_homepage, get_covid_ind

app_name = 'homepage'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('api-indonesia/', get_covid_ind, name='covid-ind'),
]