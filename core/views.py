from django.shortcuts import render
from contactos import models

# Create your views here.
def home(request):
    return render(request, 'presentation/home.html')

def agenda(request):
    contactos = models.Contactos.objects.all()
    return render(request,'presentation/agenda.html',
    {'contactos': contactos})

def about(request):
    return render(request, 'presentation/about.html')