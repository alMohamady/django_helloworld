from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Hurghada'
    dest1.des = 'It is one of the country\'s main tourist centers located on the Red Sea coast.'
    dest1.price = 200

    return render(request, 'index.html', {'dest1': dest1})
