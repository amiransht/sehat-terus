from django import forms
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect, render
from .forms import Blog_Form
from .models import Blog
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authentication.decorators import nakes_required
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def show_faqpage(request):
    return render(request, "faq.html")
    
#nampilin form
@nakes_required(login_url='/authentication/login/')
def tulis_blog(request):
    blog_form = Blog_Form()
    context = {
        'blog_form' : blog_form
    }
    return render(request, "forms.html", context)

@csrf_exempt
def submit_blog(request):
    if request.method == 'POST':
        blog = Blog.objects.create(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            author = request.user,
        )
        # print(request.user)
        return JsonResponse({
                'fields':{
                'title':blog.title,
                'content':blog.content,
            }})

def blog(request):
    return render(request, "blog.html")

def getblog(request):
    data_blog = Blog.objects.all()
    return HttpResponse(serializers.serialize("json", data_blog), content_type="application/json")
