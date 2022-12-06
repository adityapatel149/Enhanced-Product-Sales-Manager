from django.db import models
from datetime import date
# Create your models here.

class Customer(models.Model):
    first=models.CharField(max_length=15)
    last=models.CharField(max_length=15)
    email=models.EmailField()
    username=models.CharField(max_length=15,default='')
    mobile=models.IntegerField()
    password=models.CharField(max_length=8)

    def __str__(self):
        return str(self.username)
    
    
class Vendor(models.Model):
    
    cname=models.CharField(max_length=30)
    email=models.EmailField()
    username=models.CharField(max_length=15,default='')
    mobile=models.IntegerField()
    password=models.CharField(max_length=8)

    def __str__(self):
        return str(self.username)



class Pro(models.Model):
    vendor=models.ForeignKey('Vendor', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=50)
    img = models.ImageField(upload_to='app1/proimg')
    price = models.FloatField()
    review = models.TextField()
    def __str__(self):
        return self.name

