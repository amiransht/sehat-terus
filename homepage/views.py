from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_homepage(request):
    datas = Data.objects.all().values()
    context = {}
    response = {'data': datas}
    context["data"] = datas
    return render(request, "homepage.html", context=context)

def get_covid_ind(request):
    fetch_data = request.get("https://data.covid19.go.id/public/api/update.json")
    data_raw = fetch_data.json()['update']['harian'][-7:]
    labels = []
    dataMeninggal = []
    dataPositif = []
    dataRecovery = []
    
    for i in range(len(data_raw)):
        labels.append(data_raw[i]['key_as_string'][:10])
        dataMeninggal.append(data_raw[i]['jumlah_meninggal']['value'])
        dataPositif.append(data_raw[i]['jumlah_positif']['value'])
        dataRecovery.append(data_raw[i]['jumlah_sembuh']['value'])
    
    return JsonResponse(data = {
        "labels": labels,
        "dataMeninggal" : dataMeninggal,
        "dataPositif" : dataPositif,
        "dataRecovery" : dataRecovery
    }, safe=False)

@csrf_exempt
def fetch_data_prov(request):
    context = {}
    if 'query' in request.GET:
        q=request.GET['query']
        temp=Data.objects.filter(provinsi__iexact=str(q)).first()
        if (temp == None):
            errors = "Data tidak ditemukan"
        else : 
            data = temp
            response = {'positif': data.positive, 'meninggal': data.death, 'sembuh': data.recovered}
            return JsonResponse(data=response, safe=False)
    else:
        errors="Tidak ada query"
    context["errors"] = errors
    return JsonResponse(data=context, safe=False)