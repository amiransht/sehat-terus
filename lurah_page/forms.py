from django.forms import ModelForm
from lurah_page.models import DataPasien


class DataPasienForm(ModelForm):
    class Meta:
        model = DataPasien
        fields = ['nama', 'umur', 'gender', 'gejala', 'alamat']
