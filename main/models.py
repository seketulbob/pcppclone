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