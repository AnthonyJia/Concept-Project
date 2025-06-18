from django.shortcuts import render, redirect
from .models import Profile, PortfolioLink
from .forms import ProfileForm, PortfolioLinkForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

@login_required
def home(request):
    return render(request, 'portfolio/home.html')


@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)

    PortfolioLinkFormSet = modelformset_factory(
        PortfolioLink,
        form=PortfolioLinkForm,
        extra=3,
        can_delete=True
    )

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        formset = PortfolioLinkFormSet(request.POST, queryset=PortfolioLink.objects.filter(profile=profile))

        if form.is_valid() and formset.is_valid():
            form.save()

            # Save portfolio links
            links = formset.save(commit=False)
            for link in links:
                link.profile = profile
                link.save()
            for link in formset.deleted_objects:
                link.delete()

            messages.success(request, "Profile updated successfully!")
            return redirect('portfolio-home')
    else:
        form = ProfileForm(instance=profile, user=request.user)
        formset = PortfolioLinkFormSet(queryset=PortfolioLink.objects.filter(profile=profile))

    return render(request, 'portfolio/my_profile.html', {
        'form': form,
        'formset': formset,
        'profile': profile
    })
    
@login_required
def detail(request, profile_id):
    return render(request, 'portfolio/detail.html')
