from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def index(request:HttpRequest):
    return HttpResponse('<h1>hello world</h1>')

def show_int(request:HttpRequest,value: int):
    return HttpResponse(f'value is{value}')
