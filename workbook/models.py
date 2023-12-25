from django.contrib.auth import get_user_model
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(get_user_model(), related_name='workbooks')

    def __str__(self):
        return self.name


class GroupTodo(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='todos')
    todo = models.ForeignKey('todo.Task', on_delete=models.CASCADE, related_name='workbooks')

    def __str__(self):
        return f'{self.group.name} - {self.todo.title}'
