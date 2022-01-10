from django.db import models

class User_data(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
