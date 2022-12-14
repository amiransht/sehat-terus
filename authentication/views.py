from multiprocessing import context
from django.shortcuts import redirect, render
import requests
from django.http import HttpResponse
from django.core import serializers
from .forms import ProfileUpdateForm, SignUpForm, UserUpdateForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile, User
import datetime
import json
import secrets
from django.contrib import messages
from django.contrib.auth import login as auth_login
#from django.contrib.auth import login as auth_login_flutter
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .decorators import lurah_required, nakes_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
@csrf_exempt
def show_json(request):
    user = Profile.objects.all()
    data = serializers.serialize('json', user)
    return HttpResponse(data, content_type='application/json')



@csrf_exempt
def register(request):
    msg = None
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            obj = form.save()
            msg = 'Congratulations! Your account has been created. Please login to continue.'
            # print ("dict : ")
            # print (form.__dict__["fields"]["is_lurah"] == True)
            # print ("cleaned lurah sblm: ")
            # print (form.cleaned_data.get('is_lurah') == True)
            # print ("cleaned nakes: ")
            # print (form.cleaned_data.get('is_nakes') == True)
            # print ("cleaned lurah ssdh: ")
            # form.cleaned_data['is_lurah'] = False
            # print (form.cleaned_data.get('is_lurah') == True)
            # print ("fields: ")
            # print(form.fields['is_lurah'] == True)
            # print("form. :")
            # print (form.is_lurah == True)
            # print (obj.is_lurah)
            # print (obj.is_nakes)
            # obj.is_nakes = True
            # obj.save()
            # print (obj.is_nakes)
            # print(obj.username)
            # print(obj.email)
            # print(obj.password1)
            # print(obj.is_lurah)
            
            return redirect('authentication:login')
        else:
            msg = 'Oops, sorry, please check your input!'
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form, 'msg': msg})

@csrf_exempt
def login_flutter(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    data_user = Profile.objects.filter(user=user)
    notyet = "Belum tersedia"
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            print("ha")
            print(data_user[0].bio)
            print("ho")
            return JsonResponse({
                'status': True,
                'message': 'Login Success',
                'username': request.user.username,
                'is_lurah': request.user.is_lurah,
                'is_nakes': request.user.is_nakes,
                'password': request.user.password,
                'email': request.user.email,
                'first_name': data_user[0].first_name,
                'last_name': data_user[0].last_name,
                'province': data_user[0].province,
                'city': data_user[0].city,
                'bio': data_user[0].bio,
                'number_phone': data_user[0].number_phone,
                'gender': data_user[0].gender,
                'date_of_birth': "Belum tersedia",
                'district': data_user[0].district
            }, status=200)
        else:
            return JsonResponse({
                'status': False,
                'message': 'Account disabled',
            }, status=401)
    else:
        return JsonResponse({
            'status': False,
            'message': 'Invalid login',
        }, status=401)

@csrf_exempt
def register_flutter(request):
    form = SignUpForm()
    if request.method == 'POST':
        username =  request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        role_user = request.POST.get('role_user')
        form = SignUpForm(request.POST)

        if (User.objects.filter(username=username)):
            return JsonResponse({
                'status': False,
                'message': 'ERROR: Username tidak tersedia, mohon gunakan username lain',
            }, status=401)
        elif (password1 != password2):
            return JsonResponse({
                'status': False,
                'message': 'ERROR: Mohon masukkan konfirmasi password yang sama',
            }, status=401)
        # kalo udah valid semua: email bener, username ga ada yg sama, password confirm sama
        else :
            if form.is_valid():
                obj = form.save()
                obj.username = username
                obj.email = email
                obj.password1 = password1
                obj.password2 = password2
                obj.save()
                if role_user == "Lurah":
                    obj.is_lurah = True
                    obj.save()
                elif role_user == "Nakes":
                    obj.is_nakes = True
                    obj.save()
                user = authenticate(username=username, password=password1)
                data_user = Profile.objects.filter(user=user)
                return JsonResponse({
                    'status': True,
                    'message': 'Register Success',
                    'username': obj.username,
                    'is_lurah': obj.is_lurah,
                    'is_nakes': obj.is_nakes,
                    'password': obj.password,
                    'email': obj.email,
                    'first_name': "Belum tersedia",
                    'last_name': "Belum tersedia",
                    'province': "Belum tersedia",
                    'city': "Belum tersedia",
                    'bio': "Belum tersedia",
                    'number_phone': "Belum tersedia",
                    'date_of_birth': "Belum tersedia",
                    'district': "Belum tersedia",
                    'gender': "Belum tersedia", 


                }, status=200)
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Registrasi gagal! Password harus memuat 8 karakter dan minimal 1 angka / 1 huruf',
                }, status=401)

def get_dataUser_flutter(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if (user.is_authenticated):
        data_user = Profile.objects.filter(user=user)
        # return HttpResponse(serializers.serialize("json", data_user), content_type="application/json")
        return JsonResponse({
            'status': True,
            'message': 'Data User',
            'username': request.user.username,
            'is_lurah': request.user.is_lurah,
            'is_nakes': request.user.is_nakes,
            'password': request.user.password,
            'email': request.user.email,
            'first_name': data_user[0].first_name,
            'last_name': data_user[0].last_name,
            'province': data_user[0].province,
            'city': data_user[0].city,
            'bio': data_user[0].bio,
            'number_phone': data_user[0].number_phone,
            'gender': data_user[0].gender,
            'date_of_birth': data_user[0].date_of_birth,
            'district': data_user[0].district

        }, status=200)
    # return HttpResponse(serializers.serialize("json", data_user), content_type="application/json")

    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            auth_login(request,user)
            print(request.user.password)
            response = HttpResponseRedirect(reverse("homepage:show_homepage")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        elif user is not None:
            auth_login(request,user)
            print(request.user.password)
            response = HttpResponseRedirect(reverse("homepage:show_homepage")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/authentication/login/')
@lurah_required
def lurah(request):
    return render(request, 'lurahpage.html')

@login_required(login_url='/authentication/login/')
@nakes_required
def nakes(request):
    return render(request, 'nakespage.html')

def logout_user(request):
    logout(request)
    # atau ke landing page pertama
    response = HttpResponseRedirect(reverse('homepage:show_homepage'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/authentication/login/')
def profile(request):
    context = {'title': 'User Profile'}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'profil.html', context)

@login_required(login_url='/authentication/login/')
def setting(request):
    context = {}
    response = requests.get(
        'https://dev.farizdotid.com/api/daerahindonesia/provinsi').json()
    for data in response['provinsi']:
        data['nama'] = str(data['nama'])

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('authentication:profil')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context["title"] = "User Settings"
    context["response"] = response
    context["username"] = request.user.username
    context["u_form"] = u_form
    context["p_form"] = p_form
    return render(request, 'settings.html', context)

@csrf_exempt
def logout_flutter(request):
  auth_logout(request)
  return JsonResponse({
    "status": True
  }, status = 200)