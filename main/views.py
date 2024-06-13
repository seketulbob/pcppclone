import logging
from django.shortcuts import render
from .builder import display


def home(request):
    return render(request, 'home.html')

def processor(request):
    cpus = display()
    return render(request, 'processor.html', {'cpus': cpus})