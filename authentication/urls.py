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
    path('logout_flutter/', views.logout_flutter, name='logout_flutter'),
    path('login_flutter/', views.login_flutter, name='login_flutter'),
    path('register_flutter/', views.register_flutter, name='register_flutter'),
    path('get_profile/', views.get_dataUser_flutter, name='get_profile'),
    path('json/', views.show_json, name='json'),
]