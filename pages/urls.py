from django.urls import path
from .views import index, shop, product_details, signup, contact

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('shop/', shop, name='shop'),
    path('signup/', signup, name='signup'),
    path('contact/', contact, name='contact'),
    path('product-details/<int:id>/', product_details, name='product_details'),

]