# from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskPost
from .serializers import TaskPostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class TaskPostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = TaskPost.objects.all()
    serializer_class = TaskPostSerializer


# Create your views here.

@action(detail=True, methods=['post'])
def like(self, request, pk=None):
        taskPost = self.get_object()
        return Response({'status': 'Task post liked'})
