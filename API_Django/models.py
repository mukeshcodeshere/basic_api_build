import string
from django.db import models #to tell django these are models

class API_Django(models.Model): #inherit Food class from models

     #Each food has a name and a description
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=300)

     def __str__(self):
        return self.name + " " + self.description







     






