from django.db import models

class Travels(models.Model):
    ageFrom = models.IntegerField(blank=True, null=True)
    ageTo = models.IntegerField(blank=True, null=True)
    dayFrom = models.IntegerField(blank=True, null=True)
    dayTo = models.IntegerField(blank=True, null=True)
    gross = models.IntegerField(blank=True, null=True)
    net = models.IntegerField(blank=True, null=True)
    destination = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=100)  

def __str__(self):
    return self.company