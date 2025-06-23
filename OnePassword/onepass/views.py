from django.shortcuts import render
from .models import onepass_users

# Create your views here.
def index(request):
    return render(request, "onepass/index.html")

def login_page(request):

    return render(request, "onepass/login_page.html")

def signup_page(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        new_user = onepass_users(user_name=user_name, password=password)
        new_user.save()
        return render(request, "onepass/login_page.html")
    # elif request.method == "GET":
    return render(request, "onepass/signup_page.html")