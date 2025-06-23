from django.db import models

# Create your models here.
class onepass_users(models.Model):
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"user_name = {self.user_name} and password = {self.password}"