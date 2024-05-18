from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer

# Filtering task by users
class TaskListCreateView(APIView):
    """
    View to list all tasks for an authenticated user or create a new task.

    Allowed HTTP methods:
    - GET: List all tasks for the authenticated user.
    - POST: Create a new task for the authenticated user.

    Authentication is required for both methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        List all tasks for the authenticated user.

        Returns:
            Response: A list of tasks for the authenticated user.
        """
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new task for the authenticated user.

        Returns:
            Response: The created task data if the request is valid, otherwise the serializer errors.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View that handles Read Update and Delete For a particular task
class TaskRetrieveUpdateDestroyView(APIView):
    """
    View to retrieve, update, or delete a specific task for an authenticated user.

    Allowed HTTP methods:
    - GET: Retrieve a specific task for the authenticated user.
    - PUT: Update a specific task for the authenticated user.
    - DELETE: Delete a specific task for the authenticated user.

    Authentication is required for all methods.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        """
        Retrieve a specific task for the authenticated user.

        Args:
            pk (int): The primary key of the task to retrieve.

        Returns:
            Response: The requested task data if found, otherwise an HTTP 404 Not Found response.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific task for the authenticated user.

        Args:
            pk (int): The primary key of the task to update.

        Returns:
            Response: The updated task data if the request is valid, otherwise the serializer errors.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific task for the authenticated user.

        Args:
            pk (int): The primary key of the task to delete.

        Returns:
            Response: A success message if the task is deleted, otherwise an HTTP 404 Not Found response.
        """
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
