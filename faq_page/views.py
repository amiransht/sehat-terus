from django.shortcuts import render

# Create your views here.
def show_faqpage(request):
    return render(request, "faq.html")
