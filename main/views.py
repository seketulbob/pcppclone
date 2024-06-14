import logging
from django.shortcuts import render
from .builder import display_cpu, display_graphic_card, display_motherboards, display_memories, display_storages, display_cases, display_power_supplies


def home(request):
    return render(request, 'home.html')

def processor(request):
    cpus = display_cpu()
    return render(request, 'processor.html', {'cpus': cpus})

def graphic_card(request):
    graphic_cards = display_graphic_card()
    return render(request, 'graphic_card.html', {'graphic_cards': graphic_cards})

def motherboards(request):
    motherboards = display_motherboards()
    return render(request, 'motherboard.html', {'motherboards': motherboards})

def memories(request):
    memories = display_memories()
    return render(request, 'memory.html', {'memories': memories})

def storages(request):
    storages = display_storages()
    return render(request, 'storage.html', {'storages': storages})

def cases(request):
    cases = display_cases()
    return render(request, 'case.html', {'cases': cases})

def power_supplies(request):
    power_supplies = display_power_supplies()
    return render(request, 'power_supply.html', {'power_supplies': power_supplies})