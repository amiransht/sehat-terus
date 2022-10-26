from django.db import models

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
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    gender = models.CharField(max_length=10, choices= GENDER_CHOICES)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES)
    alamat = models.CharField(max_length=100)