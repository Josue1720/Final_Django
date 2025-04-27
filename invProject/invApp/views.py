from django.shortcuts import render, redirect

# Create your views here.

from .forms import ProductForm
from .models import Products
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm

def home_view(request):
    return render(request, 'invApp/home.html')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('product_list')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'invApp/login.html', {'form': form})


def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    print(form.errors)
    return render(request, 'invApp/product_form.html', {'form': form})

def product_list_view(request):
    products = Products.objects.all().order_by('-product_id')
    return render(request, 'invApp/product_list.html',{
        'products': products 
    })

def product_update_view(request,product_id):
    product = Products.objects.get(product_id= product_id)
    form = ProductForm(instance=product)
    if request.method =='POST':
        form = ProductForm(request.POST,instance = product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form}) 


def product_delete_view(request,product_id):
    product = Products.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})
    