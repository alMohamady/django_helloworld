from django.db import models

# Create your models here.


class Destination(models.Model):
    name: models.CharField(max_lenght=100)
    img: models.CharField(max_lenght=100) 
    des: models.TextField()
    price: models.IntegerField 
    spical: models.BooleanField
