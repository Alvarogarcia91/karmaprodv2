from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.template import loader
from django.db.models import *
from django.db.models import Count
from .forms import *
from datetime import *
# Create your views here.


def index(request):
    #Block_list = Block.objects.all()
    context ={
       # 'itemsfront':Block_list,
    }
    return render(request, 'index.html',context)

