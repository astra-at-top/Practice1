from django.db import models

# Create your models here.
class PasswordModle(models.Model):
    website = models.CharField(max_length=700)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=600)
    remarks = models.CharField(max_length=5000)