from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello in the index of the app!")
def  about(request):
    return HttpResponse("hello in about")

# Create your views here.
