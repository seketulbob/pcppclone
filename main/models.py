from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CPU(models.Model):
    name = models.CharField(max_length=255)  # Can contain letters and numbers
    core = models.IntegerField()  # Core counts
    socket = models.CharField(max_length=255)
    PCC = models.CharField(max_length=255)  # Performance Core Clock
    PCBC = models.CharField(max_length=255, null=True, blank=True)  # Performance Core Boost CLock
    IG = models.CharField(max_length=255, null=True, blank=True)  # Integrated Graphics
    price = models.DecimalField(max_digits=10, decimal_places=2)
    retailer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class GraphicCard(models.Model):
    name = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255, null=True, blank=True)
    memory = models.IntegerField()
    core_clock = models.IntegerField(null=True, blank=True)
    boost_clock = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    retailer = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Motherboard(models.Model):
    name = models.CharField(max_length=255)
    socket = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    memory_slots = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Memory(models.Model):
    name = models.CharField(max_length=255)
    speed = models.CharField(max_length=50)
    modules = models.CharField(max_length=50)
    cas_latency = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True, blank=True)
    form_factor = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Case(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    side_panel = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    external_volume = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class PowerSupply(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    modular = models.CharField(max_length=50)
    efficiency_rating = models.CharField(max_length=50)
    wattage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name