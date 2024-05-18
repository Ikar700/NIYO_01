from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Task(models.Model):
    """
    Model representing a task.

    Fields:
        user (ForeignKey): The user associated with the task.
        task_name (CharField): The name or title of the task.
        task_detail (TextField): The detailed description of the task.
        date_due (CharField): The due date for the task.
        created_at (DateTimeField): The date and time when the task was created.
        updated_at (DateTimeField): The date and time when the task was last updated.

    Methods:
        __str__: Returns a string representation of the task object.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    task_name = models.CharField(max_length=56)
    task_detail = models.TextField(max_length=256)
    date_due = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the task object.

        Returns:
            str: A string in the format "Task <task_name> for <user.username>".
        """
        return f"Task '{self.task_name}' for {self.user.username}"
