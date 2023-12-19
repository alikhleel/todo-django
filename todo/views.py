from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from todo.models import Task
from todo.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['GET'])
    def subtasks(self, request, pk=None):
        task = self.get_object()
        subtasks = Task.objects.filter(parent_task=task)
        serializer = TaskSerializer(subtasks, many=True)
        return Response(serializer.data)
