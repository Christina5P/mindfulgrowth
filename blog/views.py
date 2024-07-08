from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


# Create your views here.
def my_blog(request):
    return HttpResponse("Hello, Blog!")
