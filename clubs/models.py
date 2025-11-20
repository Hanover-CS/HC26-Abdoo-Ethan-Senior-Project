# clubs/models.py
# Defines the database models for the clubs app.
# Includes the Club model with fields: name, description, city, country, contact_email.

from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
