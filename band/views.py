from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import BandMember, Event
from .forms import UserRegisterForm


def render_home_page(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the home page template.
    """
    return render(request, 'band/home.html')


@login_required
def display_band_members(request):
    """
    Displays a list of band members.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the band members page with a list of band members.
    """
    band_members_list = BandMember.objects.all()
    return render(request, 'band/band_members.html', {'band_members_list': band_members_list})


@login_required
def display_upcoming_events(request):
    """
    Displays a list of upcoming events.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the events page with a list of upcoming events.
    """
    upcoming_events = Event.objects.all()
    return render(request, 'band/events.html', {'upcoming_events': upcoming_events})


def register_user(request):
    """
    Handles user registration.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the registration page, or redirects to events page after successful registration.
    """
    if request.method == 'POST':
        registration_form = UserRegisterForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            password = registration_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('events')  # Redirect to the events page
    else:
        registration_form = UserRegisterForm()
    return render(request, 'registration/register.html', {'registration_form': registration_form})


@login_required
def display_user_profile(request):
    """
    Displays the user's profile.

    Args:
        request: The HTTP request object.

    Returns:
        HTTP response rendering the profile page.
    """
    return render(request, 'registration/profile.html')


