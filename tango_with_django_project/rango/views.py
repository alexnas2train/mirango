# from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return  HttpResponse("Rango says WOW to the world!")

def about(request):
    return HttpResponse("Rango says hear about page")


