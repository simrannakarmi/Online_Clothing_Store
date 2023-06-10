from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# def login_user(request):
#     return render(request, 'members/login.html', {})

# def signup_user(request):
#     return render(request, 'members/signup.html', {})


def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            messages.success(request, ("Your password doesnot match"))
            return redirect('/users/signup_user')
        
        if pass1==pass2:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
        messages.success(request, ("Account Registered Successfully!"))
        return redirect('/users/login_user/')
    else:
        return render(request, 'users/signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print(user)

            return redirect('/')
        else:
            print(user)
            messages.success(request, ("There was an error loggin in, Try again..."))
            return redirect('/users/login_user/')
        
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

        # form = AuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     user=form.get_user()
        #     login(request, user)
        #     return redirect('onlinestore.home')

