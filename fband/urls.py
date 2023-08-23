from django.urls import path
from . import views

urlpatterns = [
    # URL for the homepage view
    path('', views.homepage, name='homepage'),

    # URL for the registration view
    path('register/', views.register, name='register'),

    # URL for the user login view
    path('login/', views.user_login, name='login'),

    # URL for the user logout view
    path('logout/', views.user_logout, name='logout'),

    # URL for the album list view
    path('album-list/', views.album_list, name='album_list'),

    # URL for the about view
    path('about/', views.about, name='about'),

    # URL for the contact view
    path('contact/', views.contact, name='contact'),
]
