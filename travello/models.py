from django.db import models

# Create your models here.


class Destination:
    id: int 
    name: str
    img: str 
    des: str
    price: int 
    spical: bool
