from django.db import models


class Place(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    display_name = models.CharField()
    display_address = models.CharField(max_length=511)
    description = models.TextField()