from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    discription=models.TextField()
    image=models.CharField(max_length=500,null=True,blank=True)
