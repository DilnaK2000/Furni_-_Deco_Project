from django.db import models

# Create your models here.

class formdb(models.Model):
    catname = models.CharField(max_length=100,null=True,blank=True)
    des = models.CharField(max_length=100,null=True,blank=True)
    img = models.ImageField(upload_to="category Images",null=True,blank=True)

class productdb(models.Model):
    category_name = models.CharField(max_length=100,null=True,blank=True)
    product_name = models.CharField(max_length=100,null=True,blank=True)
    Des = models.CharField(max_length=100,null=True,blank=True)
    pri = models.IntegerField(null=True,blank=True)
    img = models.ImageField(upload_to='Product Images',null=True,blank=True)
