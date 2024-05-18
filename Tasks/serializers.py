from rest_framework import serializers

from .models import Task

"""
Serializers for the task management app.

The serializers define the structure and validation rules for the data
that will be sent to and from the API.
"""

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    This serializer defines the fields that should be included in the
    serialized representation of a Task object, as well as any read-only
    fields or validation rules.
    """

    class Meta:
        """
        Meta class for the TaskSerializer.

        Defines the model and fields to be included in the serialized
        representation, as well as any read-only fields.
        """
        model = Task
        fields = ['id', 'user', 'task_name', 'task_detail', 'date_due', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
