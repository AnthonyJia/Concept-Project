from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, PortfolioLink
from .forms import ProfileForm, PortfolioLinkForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from django.db.models import Q


@login_required
def home(request):
    query = request.GET.get('q', '')
    
    profiles = Profile.objects.select_related('user') \
        .prefetch_related('creative_fields', 'portfoliolink_set') \
        .filter(user__is_staff=False, user__is_superuser=False)

    if query:
        profiles = profiles.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query) |
            Q(creative_fields__name__icontains=query)
        ).distinct()

    paginator = Paginator(profiles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'portfolio/home.html', {
        'page_obj': page_obj,
        'query': query,
    })

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
    profile = get_object_or_404(
        Profile.objects.select_related('user')
                       .prefetch_related('creative_fields', 'portfoliolink_set')
                       .filter(user__is_superuser=False, user__is_staff=False),
        id=profile_id
    )
    return render(request, 'portfolio/detail.html', {
        'profile': profile
    })
