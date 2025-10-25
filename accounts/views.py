from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username= username, password= password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else :
                    msg = 'Username or Password is not correct!'
                    context = {'msg' : msg}
                    return render(request,"accounts/login.html",context)
            
        form = AuthenticationForm()
        context = {"form" : form}
        return render(request, "accounts/login.html",context)
    
    else:
        return redirect("/")

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
    


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("/")
            else:
                msg = "Error"
                context = {'msg' : msg}
                return render(request, 'accounts/signup.html', context)
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)
