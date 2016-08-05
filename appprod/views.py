from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *

# Create your views here.
def listarprestadores(request):
    prestadoress=Prestador.objects.all().order_by('nome')
    lista={'prestadores':prestadoress}
    return render(request,'home.html',lista)
