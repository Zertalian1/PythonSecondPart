from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Вернет текст "Hello World"
def index(request):
    return HttpResponse('Hello World')

# Вернет текст "About"
def about(request):
    return HttpResponse('About')