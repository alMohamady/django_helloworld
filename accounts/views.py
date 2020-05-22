from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']

        if psw == psw_repeat:
            if User.objects.filter(username= username).exists():
                print('Username is already taken')
            elif User.objects.filter(email= email).exists():
                print('email is already taken')  
            else:
                user = User.objects.create_user(username= username, password= psw, email= email, first_name= first_name, last_name= last_name)
                user.save()
                print('User Saved')
        else:
            print('passwords not matching..')

        return redirect('/')
    else:
        return render(request, 'register.html')