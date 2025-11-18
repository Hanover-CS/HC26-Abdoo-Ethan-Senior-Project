from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
