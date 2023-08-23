from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User  # Import User model

# Create a custom user creation form by extending UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that extends UserCreationForm and adds an email field.

    This form is used for user registration and includes fields for username, email, and passwords.

    :param UserCreationForm: The base form for user creation provided by Django.
    :type UserCreationForm: Form class
    """

    email = forms.EmailField(required=True)
    """
    An email field for the user's email address.

    :param EmailField: A field for email addresses.
    :type EmailField: EmailField
    :param required: Indicates whether this field is required. True means it's required.
    :type required: bool
    """

    class Meta:
        model = User
        """
        The User model to use for user creation.

        :param User: The User model provided by Django's authentication system.
        :type User: Model class
        """
        fields = ('username', 'email', 'password1', 'password2')
        """
        The fields to include in the form.

        :param fields: A tuple of field names to include in the form.
        :type fields: tuple
        """
