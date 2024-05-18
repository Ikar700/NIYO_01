from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView

"""
URL patterns for the task management app.

The `urlpatterns` list maps URLs to their corresponding views.
"""

urlpatterns = [
    # URL pattern for listing all tasks or creating a new task
    path('', TaskListCreateView.as_view(), name='task-list-create'),

    # URL pattern for retrieving, updating, or deleting a specific task
    # The `<int:pk>` part captures the primary key of the task as an integer
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
]
