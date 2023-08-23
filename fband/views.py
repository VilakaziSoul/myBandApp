from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Album

def homepage(request):
    """
    Render the homepage template.

    :param request: The HTTP request object.
    :return: The rendered homepage template.
    """
    return render(request, 'fband/homepage.html')

def register(request):
    """
    Render the registration template.

    :param request: The HTTP request object.
    :return: The rendered registration template.
    """
    return render(request, 'fband/register.html')

def user_login(request):
    """
    Handle user login.

    If the HTTP request method is POST, authenticate the user and log them in.
    If login is successful, redirect to the albums page.

    If the method is not POST, render the login template with the login form.

    :param request: The HTTP request object.
    :return: The login template with the login form or a redirect to the albums page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the albums page if login is successful
                return redirect('album_list')
    else:
        form = AuthenticationForm()
    # Render the login template with the form
    return render(request, 'fband/login.html', {'form': form})

@login_required(login_url='login', redirect_field_name=None)
def user_logout(request):
    """
    Handle user logout.

    Log the user out and redirect to the homepage.

    :param request: The HTTP request object.
    :return: A redirect to the homepage.
    """
    logout(request)
    # Redirect to the homepage after logout
    return redirect('homepage')

@login_required(login_url='login', redirect_field_name=None)
def album_list(request):
    """
    Render the album list page.

    Retrieve all albums and render the album list template with the albums.

    :param request: The HTTP request object.
    :return: The album list template with the albums.
    """
    albums = Album.objects.all()
    # Render the album list template with the albums
    return render(request, 'fband/album_list.html', {'albums': albums})

@login_required(login_url='login', redirect_field_name=None)
def about(request):
    """
    Render the about page.

    :param request: The HTTP request object.
    :return: The rendered about template.
    """
    # Render the about template
    return render(request, 'fband/about.html')

@login_required(login_url='login', redirect_field_name=None)
def contact(request):
    """
    Render the contact page.

    :param request: The HTTP request object.
    :return: The rendered contact template.
    """
    # Render the contact template
    return render(request, 'fband/contact.html')
