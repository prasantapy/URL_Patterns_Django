from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def demo(request):
    return HttpResponse('it is app-2 page')
