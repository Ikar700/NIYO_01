from django.contrib import admin
from django.urls import path, include

"""
Root URL configuration for the project.

The `urlpatterns` list maps URLs to their corresponding views or URL patterns.
"""

urlpatterns = [
    # URL pattern for the Django admin site
    path("admin/", admin.site.urls),

    # URL pattern for the authentication app
    # Includes the URL patterns defined in the "Auth.urls" module
    path('api/auth/', include("Auth.urls")),

    # URL pattern for the task management app
    # Includes the URL patterns defined in the "Tasks.urls" module
    path('api/tasks/', include("Tasks.urls"))
]
