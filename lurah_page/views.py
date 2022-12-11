from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse  # , HttpResponseRedirect
# from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import datetime

from lurah_page.models import DataPasien
from lurah_page.forms import DataPasienForm

from authentication.decorators import lurah_required


# Create your views here.

@login_required(login_url='authentication:login')
@lurah_required
def show_lurah_homepage(request):
    return render(request, 'lurah_homepage.html')


@login_required(login_url='authentication:login')
@lurah_required
def show_lurah_page(request):
    data_pasien = DataPasien.objects.filter(user=request.user)
    context = {'data_pasien': data_pasien,
               'user': request.user
               }
    return render(request, 'lurah_pasien.html', context)


@login_required(login_url='authentication:login')
@lurah_required
def add_pasien(request):
    form = DataPasienForm()
    if request.method == 'POST':
        form = DataPasienForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('lurah_page:show_lurah_page')

    context = {'form': form}
    return render(request, 'add_pasien.html', context)


@csrf_exempt
def add_pasien_ajax(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        umur = request.POST.get('umur')
        gender = request.POST.get('gender')
        gejala = request.POST.get('gejala')
        alamat = request.POST.get('alamat')
        todo = DataPasien.objects.create(
            nama=nama, umur=umur, gender=gender, gejala=gejala, alamat=alamat, is_covid=True, user=request.user)
        serialize_json = serializers.serialize('json', [todo])
        print(serialize_json)
        return HttpResponse(serialize_json)

    return JsonResponse({'error': "Not an ajax request"}, status=404)


@csrf_exempt
def delete_pasien(request, id):
    if request.method == 'DELETE':
        task = get_object_or_404(DataPasien, id=id)
        task.delete()
    return HttpResponse(status=202)


@login_required(login_url='authentication:login')
@lurah_required
def show_json(request):
    data_pasien = DataPasien.objects.filter(user=request.user)
    data = serializers.serialize('json', data_pasien)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def add_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        nama = data['nama']
        umur = data['umur']
        gender = data['gender']
        gejala = data['gejala']
        alamat = data['alamat']
        try:
            DataPasien.objects.get(nama=nama, alamat=alamat)
            return JsonResponse({"status": "dup"}, status=401)
        except:
            addPasien = DataPasien.objects.create(
            nama = nama,
            umur = umur,
            gender = gender,
            gejala = gejala,
            alamat = alamat,
            )

            addPasien.save()

            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
