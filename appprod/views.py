from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *

# Create your views here.
def listarprestadores(request):
    prestadores=Prestador.objects.all().order_by('nome')
    lista={'prestadores':prestadores}
    return render(request,'home.html',lista)
