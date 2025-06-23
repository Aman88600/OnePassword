from django.shortcuts import render
from .models import onepass_users, onepass_text

# Create your views here.
def index(request):
    return render(request, "onepass/index.html")

def login_page(request):
    if request.method == "POST":
        try:
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            user = onepass_users.objects.get(user_name=user_name)
            if user.password == password:
                user_entries = onepass_text.objects.filter(user_name=user_name)
                user_text = [entry.user_data for entry in user_entries]
                return render(request, "onepass/dashboard.html", {"user_name" : user_name, "user_text" : user_text})
            else:
                return render(request, "onepass/login_page.html")
        except onepass_users.DoesNotExist:
            return render(request, "onepass/login_page.html")
    return render(request, "onepass/login_page.html")

def dashboard(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        pre_text = request.POST.get("previous_text")
        user_text = request.POST.get("text")
        new_entry = onepass_text(user_name=user_name, user_data=user_text)
        new_entry.save()
        user_entries = onepass_text.objects.filter(user_name=user_name)
        user_text = [entry.user_data for entry in user_entries]
    return render(request, "onepass/dashboard.html", {"user_name" : user_name, "user_text" : user_text})
    
def signup_page(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        new_user = onepass_users(user_name=user_name, password=password)
        new_user.save()
        return render(request, "onepass/login_page.html")
    # elif request.method == "GET":
    return render(request, "onepass/signup_page.html")