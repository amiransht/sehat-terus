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

from lurah_page.models import DataPasien


from authentication.decorators import nakes_required


# Create your views here.
@login_required(login_url='authentication:login')
@nakes_required
def show_nakes_homepage(request):
    return render(request, 'nakes_homepage.html')

@login_required(login_url='authentication/login/')
@nakes_required
def show_nakes_page(request):
    data_pasien = DataPasien.objects.all()
    context = {'data_pasien': serializers.serialize('json', data_pasien),
               'user': request.user
               }
    return render(request, 'nakes.html', context)

@login_required(login_url='authentication/login/')
def show_json(request):
    data_pasien = DataPasien.objects.all()
    data = serializers.serialize('json', data_pasien)
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='authentication/login/')
@nakes_required
def update_status_pasien(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'UPDATE':
        pasien = DataPasien.objects.filter(pk=id)
        status_pasien = DataPasien.objects.get(pk=id).is_covid
        print(DataPasien.objects.get(pk=id).is_covid)
        if status_pasien == True:
            pasien.update(is_covid = False)
        else:
            pasien.update(is_covid = True)
        DataPasien.objects.get(pk=id).save()
        print(DataPasien.objects.get(pk=id).is_covid)
        result = DataPasien.objects.filter(pk=id)
        data = serializers.serialize('json', result)
        return HttpResponse(data, content_type='application/json') 

    return JsonResponse({'error': "Not an ajax request"}, status=400)
    