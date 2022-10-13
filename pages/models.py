from django.db import models
import math
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    subId = models.ForeignKey(Category, related_name='subcategory', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    img = models.ImageField(null=True)
    title = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Category, related_name='category',on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, related_name='brand',on_delete=models.SET_NULL, null=True)
    narx = models.IntegerField(null=True)
    chegirma = models.IntegerField(default=0, null=True)
    soni = models.IntegerField(null=True, default=0)
    holati = models.CharField(max_length=255,null=True)
    def ayir(self):
        return math.floor(self.narx - ((self.narx*self.chegirma)/100))

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255,  blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name