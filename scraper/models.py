from django.db import models

# Create your models here.

class LinkAdress( models.Model):
    
    name = models.CharField( max_length = 500, null = True, blank= True)
    address = models.CharField( max_length = 1000, null = True, blank= True)

    def __str__(self):
        return f' {self.name} '