# Import some neccessary moduls
from django.urls import path
from . import views


# URL pattern definitions for the band app
urlpatterns = [

    # Home page URL
    path('', views.home, name='home'),

    # Band members page URL
    path('members/', views.band_members, name='band_members'),

    # Events page URL
    path('events/', views.events, name='events'),

    # Register page URL
    path('register/', views.register, name='register'),

    # Profile page URL 
    path('profile/', views.profile, name='profile'),
]

