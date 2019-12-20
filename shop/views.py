from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
#from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout



def index(request):
	text_var = 'This is my first django app web page.'
	return HttpResponse(text_var)

#Category view

def allProdCat(request, c_slug=None):
	c_page = None
	products_list = None
	if c_slug!=None:
		c_page = get_object_or_404(Category,slug=c_slug)
		products_list = Product.objects.filter(category=c_page,available=True)
	else:
		products_list = Product.objects.all().filter(available=True)
	'''Pagination code'''
	paginator = Paginator(products_list, 6)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
		products_list = Product.objects.all().filter(available=True)
	return render(request,'shop/category.html',{'category':c_page,'products_list':products_list})

def ProdCatDetail(request,c_slug,product_slug):
	try:
		product = Product.objects.get(category__slug=c_slug,slug=product_slug)
	except Exception as e:
		raise e
	return render(request,'shop/product.html', {'product':product})




def pruebadisplays(request):
    products = Product.objects.all().filter(available=True)
    context ={
        'itemsfront':products,
    }

    
    return render(request, 'pruebadisplays.html',context)