from django.shortcuts import render
from django.views.generic import ListView
from .models import Meme

"""def home(request):
    return render(request, "main/home.html", context={})"""

def signup(request):
    return render(request, "main/signup.html", context={})

def signuppost(request):
    return

class HomePageView(ListView):
    model = Meme
    template_name = "main/home.html"
