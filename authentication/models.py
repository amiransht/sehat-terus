from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_lurah = models.BooleanField('is_lurah',default=False)
    is_nakes = models.BooleanField('is_nakes',default=False)

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default="Belum Tersedia")
    last_name = models.CharField(max_length=200, default="Belum Tersedia")
    province = models.CharField(max_length=200, default="Belum Tersedia")
    bio = models.CharField(max_length=200, default="Belum Tersedia")
    city = models.CharField(max_length=200, default="Belum Tersedia")
    gender = models.CharField(max_length=200, default="Belum Tersedia")
    number_phone = models.CharField(max_length=200, default="Belum Tersedia")
    date_of_birth = models.DateField(null=True)
    district = models.CharField(max_length=200, default="Belum Tersedia")
    image = models.ImageField(default="default.jpg",upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username}-Profile'
