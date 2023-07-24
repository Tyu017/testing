from django.db import models

# Create your models here.
class form(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=13)
    email = models.EmailField()
    destination = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
