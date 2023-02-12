from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile_edit(request):
    """
    Display the user's profile to edit
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
            return redirect('home')

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile_edit.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def profile(request):
    """
    Display users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
