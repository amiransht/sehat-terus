from django.urls import include, path
from . import views
from homepage.views import show_homepage

app_name = 'authentication'

urlpatterns = [
    path('', show_homepage, name= 'index'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('register/', views.register, name= 'register'),
    path('profil/', views.profile, name='profil'),
    path('setting/', views.setting, name='setting'),
]