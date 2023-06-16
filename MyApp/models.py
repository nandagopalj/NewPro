from django.db import models

# Create your models here.

class Categorydb(models.Model):
    Category_Name = models.CharField(max_length=20, null=True, blank=True)
    Category_Image = models.ImageField(upload_to="Category Image", null=True, blank=True)
    Category_Description = models.CharField(max_length=100, null=True, blank=True)

class Productdb(models.Model):
    Category_Name = models.CharField(max_length=20, null=True, blank=True)
    Product_Name = models.CharField(max_length=20, null=True, blank=True)
    Product_Price = models.IntegerField(null=True, blank=True)
    Product_Description = models.CharField(max_length=100, null=True, blank=True)
    Product_Image = models.ImageField(upload_to="Product Image", null=True, blank=True)

class Contactdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Mobile = models.CharField(max_length=20, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
