from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.urls import reverse


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("pizza:index")
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "pizza/index.html", {"message": "Logged out."})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('pizza:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})