from django.urls import path, include

from . import views

# url patterns for djoser to create a new user 
urlpatterns = [
    path('', include('djoser.urls')),
    path('login/', views.LoginView.as_view(), name='login')
]