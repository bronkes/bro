from django.shortcuts import render

from .models import *
# Create your views here.

def index(request):
    menus=Menu.objects.values()
    context = {'menus': menus}
    return render(request, 'index.html', context)