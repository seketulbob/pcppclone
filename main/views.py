import logging
from django.shortcuts import render
from .builder import display_cpu, display_graphic_card


def home(request):
    return render(request, 'home.html')

def processor(request):
    cpus = display_cpu()
    return render(request, 'processor.html', {'cpus': cpus})

def graphic_card(request):
    graphic_cards = display_graphic_card()
    return render(request, 'graphic_card.html', {'graphic_cards': graphic_cards})