from django.urls import include, path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('register/', views.register, name= 'register'),
    path('home/', views.home, name= 'home'),
    path('lurah/', views.lurah, name= 'lurah'),
    path('nakes/', views.nakes, name= 'nakes'),
    path('profil/', views.profile, name='profil'),
    path('setting/', views.setting, name='setting'),
    path('delete-user/', views.delete_user, name='delete-user'),
]