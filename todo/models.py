from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200, blank=True)
    completed = models.BooleanField(default=False, null=True)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtasks')
    created = models.DateTimeField(auto_now_add=True)
    end_data = models.DateTimeField(blank=True, default=timezone.now() + timezone.timedelta(days=1))
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
