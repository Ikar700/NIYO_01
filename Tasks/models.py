from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
    task_name = models.CharField(max_length=56)
    task_detail = models.TextField(max_length=256)
    date_due = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Task {self.task_name} for {self.user.username}"