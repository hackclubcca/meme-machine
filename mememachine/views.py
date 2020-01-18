from django.shortcuts import render

def home(request):
    return render(request, "index.html", context={})

def signup(request):
    return render(request, "signup.html", context={})

def signuppost(request):
    return