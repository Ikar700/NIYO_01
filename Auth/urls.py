from django.urls import path, include

from . import views

"""
URL patterns for user authentication.

This module defines the URL patterns for user authentication,
including user registration and login.
"""

# url patterns for djoser to create a new user
urlpatterns = [
    # URL patterns for Djoser's built-in authentication views
    # Includes URLs for user registration, password reset, and more
    path('', include('djoser.urls')),

    # URL pattern for the custom login view
    path('login/', views.LoginView.as_view(), name='login')
]
