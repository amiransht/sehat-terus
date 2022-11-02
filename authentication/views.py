from multiprocessing import context
from django.shortcuts import redirect, render
import requests
from .forms import ProfileUpdateForm, SignUpForm, LoginForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .decorators import lurah_required, nakes_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def register(request):
    msg = None
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Congratulations! Your account has been created. Please login to continue.'
            return redirect('authentication:login')
        else:
            msg = 'Oops, sorry, please check your input!'
    else:
        form = SignUpForm()
        
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_lurah:
            auth_login(request,user)
            response = HttpResponseRedirect(reverse("homepage:show_homepage")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        elif user is not None and user.is_nakes:
            auth_login(request,user)
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
