from .models import CPU, GraphicCard, Motherboard, Memory, Storage, Case, PowerSupply

def display_cpu():
    return CPU.objects.all()

def display_graphic_card():
    return GraphicCard.objects.all()

def display_motherboards():
    return Motherboard.objects.all()

def display_memories():
    return Memory.objects.all()

def display_storages():
    return Storage.objects.all()

def display_cases():
    return Case.objects.all()

def display_power_supplies():
    return PowerSupply.objects.all()
