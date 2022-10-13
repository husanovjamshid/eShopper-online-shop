from django.shortcuts import render, redirect
from .models import Category, Brand, Product, Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.

def index(req):
    return render(req, 'index.html',)

def shop(req):
    ct = Category.objects.all()
    brand = Brand.objects.all()
    products = Product.objects.all()

    page = req.GET.get('page', 1)

    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(req, 'shop.html',context={
        'ct':ct,
        'brand':brand,
        # 'product':product,
        'products': products
    })

def product_details(req, id):
    brand = Brand.objects.all()
    proDetail = Product.objects.get(id=id)
    return render(req, 'product_details.html', context={
        'proDetail':proDetail,
        'brand':brand
    })



def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')

            return redirect('index')
        else:
            messages.error(request, 'Errorr')

    return render(request, 'registration/signup.html', context={
        'form': form
    })

def contact(request):
    contact = Contact()

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
            messages.success(request, 'Xabaringiz muvaffaqqiyatli yetkazildi!!!')
        except:
            messages.error(request, 'Xabaringiz yuborilmadi!!!')


    return render(request, 'contact.html',
                  context={

                  }
                  )




