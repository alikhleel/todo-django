from django.contrib.auth import get_user_model
from django.db import models


class Workbook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_workbooks')
    users = models.ManyToManyField(get_user_model(), related_name='workbooks')

    def __str__(self):
        return self.name


class WorkbookTodo(models.Model):
    group = models.ForeignKey(Workbook, on_delete=models.CASCADE, related_name='todos')
    todo = models.ForeignKey('todo.Task', on_delete=models.CASCADE, related_name='workbooks')

    def __str__(self):
        return f'{self.group.name} - {self.todo.title}'


class WorkbookUserPermission(models.Model):
    workbook = models.ForeignKey(Workbook, on_delete=models.CASCADE, related_name='permissions')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='workbook_permissions')
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.can_edit}'
