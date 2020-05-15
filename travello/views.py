from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Hurghada'
    dest1.des = 'It is one of the country\'s main tourist centers.'
    dest1.img = 'hurghada.jpg'
    dest1.price = 200

    dest2 = Destination()
    dest2.name = 'Cairo'
    dest2.des = 'Cairo is the capital of Egypt .'
    dest2.img = 'cairo.jpg'
    dest2.price = 400

    dest3 = Destination()
    dest3.name = 'Alexandria'
    dest3.des = 'Alexandria is the second-largest city in Egypt.'
    dest3.img = 'alexandria.jpg'
    dest3.price = 500

    dest = [ dest1, dest2, dest3 ]

    return render(request, 'index.html', {'dest': dest})
