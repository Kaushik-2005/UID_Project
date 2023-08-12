from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(username, password, user)
        if user is not None:
            print("hi user")
            auth.login(request, user)
            return redirect('index')
        else:
            print(" invalid")
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else: 
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    return render(request,'register.html')




def verify(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        cpassword = request.POST.get('password2')

        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email exists..!')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username exists..!')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            return redirect('register')
        else:
            print('Passwords do not match!')
            return redirect('register')
        
    else: 
        return redirect('register')
