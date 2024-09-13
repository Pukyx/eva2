from django.shortcuts import render

# Create your views here.

def render(request): 
    return request  

def peli1(request):
    data = {'nombre': 'Barbie y el Secreto de las Hadas','Descripción':'', 'valoración': 4} 
    return request 

def peli2(request):
    data = {'nombre': 'Barbie Fairytopia','Descripción':'', 'valoración': 5} 
    return request

def peli3(request):
    data = {'nombre': 'Barbie y las 12 princesas bailarinas','Descripción':'', 'valoración': 0} 
    return request