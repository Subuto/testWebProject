from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #print(request)
    return HttpResponse('Hello')

def test(request):
    #print(request)
    return HttpResponse('<h1>Hello</h1>')
# Create your views here.
