from django.db import models

# Create your models here.
class contactdb(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email_ad=models.EmailField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)

class signupdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    pas1 = models.CharField(max_length=100, null=True, blank=True)
    pas2 = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='Save Images', null=True, blank=True)

class cartdb(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    proname = models.CharField(max_length=100, null=True, blank=True)
    quantity =  models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

