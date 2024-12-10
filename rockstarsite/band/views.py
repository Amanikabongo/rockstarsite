from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import BandMember, Event
from .forms import UserRegisterForm


def home(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the home page template.
    """
    return render(request, 'band/home.html')


@login_required
def band_members(request):
    """
    Displays a list of band members.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the band members page with a list of band members.
    """
    members = BandMember.objects.all()
    return render(request, 'band/band_members.html', {'members': members})


@login_required
def events(request):
    """
    Displays a list of upcoming events.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the events page with a list of upcoming events.
    """
    events = Event.objects.all()
    return render(request, 'band/events.html', {'events': events})


def register(request):
    """
    Handles user registration.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the registration page, or redirects to events page after successful registration.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('events')  # Redirect to the events page
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """
    Displays the user's profile.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the profile page.
    """
    return render(request, 'registration/profile.html')

