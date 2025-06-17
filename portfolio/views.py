from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def my_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('portfolio-my-profile')  # or use reverse_lazy
    else:
        form = ProfileForm(instance=profile, user=request.user)

    return render(request, 'portfolio/my_profile.html', {
        'form': form,
        'profile': profile
    })
    

def detail(request, profile_id):
    return render(request, 'portfolio/detail.html')
