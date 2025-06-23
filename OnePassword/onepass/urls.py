from django.urls import path
from . import views

# app_name
app_name = "onepass"

# Url Patterns
urlpatterns = [path("", views.index, name="index"),
               path("login_page", views.login_page, name="login_page"),
               path("signup_page", views.signup_page, name="signup_page"),
               path("dashboard", views.dashboard, name="dashboard")]