from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_lurah = models.BooleanField('is_lurah',default=False)
    is_nakes = models.BooleanField('is_nakes',default=False)

class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    number_phone = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    daftar_rs = models.CharField(max_length=1000, null=True)
    district = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f'{self.user.username}-Profile'
