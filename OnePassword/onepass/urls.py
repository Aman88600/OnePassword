from django.urls import path
from . import views

# app_name
app_name = "onepass"

# Url Patterns
urlpatterns = [path("", views.index, name="index")]