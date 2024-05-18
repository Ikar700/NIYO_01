from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'task_name', 'task_detail', 'date_due', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
