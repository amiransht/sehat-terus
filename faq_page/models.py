from unittest.util import _MAX_LENGTH
from django.db import models
from authentication.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
