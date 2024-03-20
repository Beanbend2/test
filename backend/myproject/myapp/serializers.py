from rest_framework import serializers
from .models import TaskPost

class TaskPostSerializer(serializers.ModelSerializer):
	class Meta:
            model = TaskPost
            fields = ['id', 'title', 'content', 'published_date']

