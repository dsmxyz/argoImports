from django.db import models

# Create your models here.

class Customer(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=20)
    
    def __str__(self):
        return(f"{self.name}")
    
class Truck(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50)
    make=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    vin=models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.year} {self.make} {self.model} ({self.name})")
