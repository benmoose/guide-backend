from django.db import models


class Place(models.Model):
    """
    The DB model for a Place.
    """
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    display_name = models.CharField(max_length=255)
    display_address = models.CharField(max_length=511)
    description = models.TextField(blank=True)
