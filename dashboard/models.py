from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Bitcoin(models.Model):
    amount = models.IntegerField()
    wallet = models.TextField(max_length=100)
    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 

class Paypal(models.Model):
    amount = models.IntegerField()
    email = models.TextField(max_length=100)
    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 

class Deposits(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    deposit_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.username 


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(blank=True, default='0',)
    deposit = models.IntegerField(blank=True, default='0',)
    earning = models.IntegerField(blank=True, default='0',)
    fee = models.IntegerField(blank=True, default='0',)
    deposit_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='username',)

    def __str__(self): 
        return self.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sn = models.IntegerField(blank=True)
    type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default = 'Username')
    
    def __str__(self):
        return self.name

class Fusion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    capital = models.IntegerField(blank=True, default='0',)
    profit = models.IntegerField(blank=True, default='0',)
    balance = models.IntegerField(blank=True, default='0',)
    # fee = models.IntegerField(blank=True)
    status = models.BooleanField()
    username = models.CharField(max_length=100, blank=True, default='username',)

    def __str__(self):
        return self.username


class HubRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.BigIntegerField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=200, blank=True)
    income = models.CharField(max_length=100, blank=True)
    marital = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self): 
        return self.email 


