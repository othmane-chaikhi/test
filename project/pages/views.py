from django.shortcuts import render
from django.http  import HttpResponse 
from .models import Person

def index(request):
    return render(request, 'home/index.html')
def login(request):
    return render(request,'home/login.html')
def persons(request):
    return render(request,'home/persons.html',{'persons':Person.objects.all()})
