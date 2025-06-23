from django.contrib import admin
from .models import onepass_users, onepass_text
# Register your models here.
admin.site.register(onepass_users)
admin.site.register(onepass_text)
