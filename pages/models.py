from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    # country = models.CharField(max_length=100, blank=True)
    phone = models.BigIntegerField(blank=True)
    message = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self): 
        return self.name 





    





    

