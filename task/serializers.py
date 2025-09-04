from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'priority',
            'due_date',
            'start_date',
            'completed_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at']
