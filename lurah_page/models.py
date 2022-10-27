from email.policy import default
from django.db import models
from authentication.models import User

# Create your models here.
GENDER_CHOICES = (
    ('laki', 'Laki-laki'),
    ('perempuan', 'Perempuan'),
)

STATUS_CHOICES = (
    ('nogejala', 'Tanpa Gejala'),
    ('gejalasedang', 'Gejala Sedang'),
    ('gejalaberat', 'Gejala Berat'),
)


class DataPasien(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    gejala = models.CharField(max_length=100, choices=STATUS_CHOICES)
    alamat = models.CharField(max_length=100)
