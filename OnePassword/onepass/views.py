from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "onepass/index.html")

def login_page(request):
    return render(request, "onepass/login_page.html")

def signup_page(request):
    return render(request, "onepass/signup_page.html")