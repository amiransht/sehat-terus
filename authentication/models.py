from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_lurah = models.BooleanField('is_lurah',default=False)
    is_nakes = models.BooleanField('is_nakes',default=False)
    