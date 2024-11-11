from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения Agencies.")

def groups(request, group): 
    if request.GET: 
        print(request.GET)
    return HttpResponse(f"<h1>Список агентов. </h1><h2>{group}</h2>")