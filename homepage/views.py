from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests as req

# Create your views here.
def show_homepage(request):
    datas = Data.objects.all()
    context = {'data' : datas}
    return render(request, "homepage.html", context)

def get_covid_api(request):
    fetch_data = req.get("https://data.covid19.go.id/public/api/prov.json")
    data_raw = fetch_data.json()

    return JsonResponse(data = {
        "data" : data_raw
    }, safe=False)


def search_prov(request):
    array_prov = ["DKI JAKARTA", "JAWA BARAT", "JAWA TIMUR", "BANTEN", ]
    if request.method == 'POST':
        nama_prov = request.POST['nama_prov']
        buat_barang = Data.objects.create(
            provinsi = nama_prov

        )
        return JsonResponse(
            {
                'error':False,
                'msg':'Success'
            }
        )
    return redirect('homepage:show_homepage')
