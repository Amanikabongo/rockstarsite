from django.db import models
from django.contrib.auth.models import User


class BandMember(models.Model):
    """
    Model representing a band member.
    Attributes:
        name (str): The name of the band member.
        instrument (str): The instrument played by the band member.
        bio (str): A short biography of the band member.
        user (ForeignKey): A one-to-one relationship to the User model.
    """
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Model representing a band event.
    Attributes:
        title (str): The title of the event.
        description (str): A detailed description of the event.
        date (datetime): The date and time of the event.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title




