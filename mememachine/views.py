from django.shortcuts import render
from django.views.generic import ListView

def home(request):
    return render(request, "index.html", context={})

def signup(request):
    return render(request, "signup.html", context={})

def signuppost(request):
    return

class HomePageView(ListView):
    model = Meme
    template_name = "main/home.html"
