from django.urls import path
from . import views

# Define the namespace for the app URLs
app_name = 'user_auth'

urlpatterns = [
    # URL for user registration view
    path('register/', views.register, name='register'),
    
    # URL for user login view
    path('login/', views.user_login, name='login'),
    
    # URL for user logout view
    path('logout/', views.user_logout, name='logout'),
]
