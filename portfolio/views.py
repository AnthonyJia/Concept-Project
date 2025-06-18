from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'portfolio/home.html')

@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('portfolio-home')  # or use reverse_lazy
    else:
        form = ProfileForm(instance=profile, user=request.user)

    return render(request, 'portfolio/my_profile.html', {
        'form': form,
        'profile': profile
    })
    
@login_required
def detail(request, profile_id):
    return render(request, 'portfolio/detail.html')
