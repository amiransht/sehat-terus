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

from nakes_page.models import DataPasien

# Create your views here.
@login_required(login_url='authentication/login/')
def show_nakes_page(request):
    data_pasien = DataPasien.objects.all()
    context = {'data_pasien': serializers.serialize('json', data_pasien),
               'user': request.user
               }
    return render(request, 'nakes.html', context)

@login_required(login_url='authentication/login/')
def show_json(request):
    data_pasien = DataPasien.objects.filter.all()
    data = serializers.serialize('json', data_pasien)
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='authentication/login/')
def update_status_pasien(request, id_pasien):
    status_pasien = DataPasien.objects.get(id=id_pasien).status
    if status_pasien == True:
        status_pasien = False
    else:
        status_pasien = True
    status_pasien.save()
    return redirect('nakes_page:show_nakes_page')