"""Project models"""
from django.db import models


class Proposal(models.Model):
    full_name = models.CharField(max_length=150)
    taxpayer_identification = models.CharField(max_length=17)
    loan_value = models.DecimalField(max_digits=12, decimal_places=2)


class Address(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=250)
    number = models.PositiveSmallIntegerField()
    complement = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=8)
