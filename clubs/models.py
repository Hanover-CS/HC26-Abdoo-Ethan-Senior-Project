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

    from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # optional
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    club = models.ForeignKey('Club', on_delete=models.CASCADE, null=True, blank=True)  # optional link to a club

    def __str__(self):
        return {self.title} 

