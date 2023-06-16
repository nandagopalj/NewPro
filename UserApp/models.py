from django.db import models

# Create your models here.

class Userdb(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    Mobile = models.CharField(max_length=20, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)
    Profile_Image = models.ImageField(upload_to="Profile Image", null=True, blank=True)

class Cartdb(models.Model):
    Username = models.CharField(max_length=20, null=True, blank=True)
    Product_Name = models.CharField(max_length=20, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)

class Checkoutdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Contact = models.CharField(max_length=20, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    PIN = models.CharField(max_length=10, null=True, blank=True)
