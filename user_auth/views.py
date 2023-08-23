from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm  # Import your custom form

def register(request):
    """
    Handle user registration.

    If the HTTP request method is POST, attempt to register the user using the provided form data.
    If registration is successful, log in the user and redirect to the albums page.

    If the method is not POST, render the registration template with an empty registration form.

    :param request: The HTTP request object.
    :return: The registration template with the registration form or a redirect to the albums page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after registration
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user)
            return redirect('album_list')  # Redirect to the albums page
    else:
        form = CustomUserCreationForm()
    return render(request, 'fband/register.html', {'form': form})

def user_login(request):
    """
    Handle user login.

    If the HTTP request method is POST, attempt to authenticate and log in the user using the provided form data.
    If login is successful, redirect to the homepage or another desired location.

    If the method is not POST, render the login template with the login form.

    :param request: The HTTP request object.
    :return: The login template with the login form or a redirect to the homepage or another desired location.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to home page or desired location
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    """
    Handle user logout.

    Log out the user and redirect to the homepage or another desired location.

    :param request: The HTTP request object.
    :return: A redirect to the homepage or another desired location.
    """
    logout(request)
    return redirect('homepage')  # Redirect to home page or desired location
