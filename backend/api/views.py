from django.shortcuts import render
from django.http import HttpResponse, request

def home(request):
    return HttpResponse("This is the homepage")



# Create your views here.
