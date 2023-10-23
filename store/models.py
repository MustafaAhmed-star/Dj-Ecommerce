from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=200,null = True)
    email = models.CharField(max_length=200,null = True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True)
    #image
    def __str__(self):

        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False,blank=True,null=True)
    transaction_id = models.CharField(max_length=200,null = True)


    def __str__(self) -> str:
        return f'Order for{self.customer}'
    