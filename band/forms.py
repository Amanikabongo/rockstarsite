from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """
    Custom user registration form inheriting from UserCreationForm.

    Attributes:
        email (EmailField): Email field for the registration form.

    Meta:
        model (User): The model associated with this form.
        fields (list): List of fields to be included in the form.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

