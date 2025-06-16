from django.shortcuts import render
from .models import Profile

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def my_profile(request):
    return render(request, 'portfolio/my_profile.html')

def detail(request, profile_id):
    return render(request, 'portfolio/detail.html')
