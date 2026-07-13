from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField()       
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.IntegerField(default=5)     
    status = models.CharField(max_length=50, default="Mavjud") 
    brand = models.CharField(max_length=100, default="Noma'lum") 
    color = models.CharField(max_length=50, default="Standart") 

    def __str__(self):
        return self.name