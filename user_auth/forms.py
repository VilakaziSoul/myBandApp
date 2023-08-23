from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User  # Import User model

# Create a custom user creation form by extending UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
