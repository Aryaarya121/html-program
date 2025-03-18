from django.db import models

from django.contrib.auth.models import User

# Blood Bank Model
class BloodBank(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Donor Model
class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
