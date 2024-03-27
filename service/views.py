from django.shortcuts import render
from .models import Service

# Create your views here.
def sercicios(req):

    service = Service.objects.all()

    return render(req, 'service/servicios.html' , {'service': service})