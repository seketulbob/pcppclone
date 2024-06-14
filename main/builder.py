from .models import CPU, GraphicCard

def display_cpu():
    return CPU.objects.all()

def display_graphic_card():
    return GraphicCard.objects.all()
