from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests as req
from authentication.views import login
from lurah_page.models import DataPasien

# Create your views here.
def show_homepage(request):
    return render(request, "homepage.html")

def get_covid_api(request):
    fetch_data = req.get("https://data.covid19.go.id/public/api/prov.json")
    data_raw = fetch_data.json()
    data_parse = data_raw['list_data']

    for i in range(len(data_parse)):
        new_data = Data.objects.create(
            provinsi = data_parse[i]['key'],
            positive = data_parse[i]['jumlah_kasus'] - data_parse[i]['jumlah_sembuh'],
            death = data_parse[i]['jumlah_meninggal'],
            recovered = data_parse[i]['jumlah_sembuh']
        )
    return JsonResponse(data = data_parse, safe=False)


def show_json_pasien(request):
    data_pasien = DataPasien.objects.all()
    data = serializers.serialize('json', data_pasien)
    return HttpResponse(data, content_type='application/json')

 
