from django.shortcuts import render

# Create your views here.
def show_lurah_page(request):
    return render(request, "lurah.html")