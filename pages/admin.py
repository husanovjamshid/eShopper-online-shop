from django.contrib import admin
from .models import Category, Brand, Product, Contact, SubCategory
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','brand', 'category', 'narx')
admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date', 'message')
admin.site.register(Contact, ContactAdmin)