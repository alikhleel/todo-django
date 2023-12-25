from unittest import TestCase

from django.contrib.auth import get_user_model

from todo.models import Task
from workbook.models import Group, GroupTodo

User = get_user_model()


class WorkbookTests(TestCase):
    def test_group_model_has_many_users(self):
        user = User.objects.create_user(email="ali@ali.com", password="test456")
        user2 = User.objects.create_user(email="ali1@ali.com", password="test456")
        group = Group.objects.create(name="test", description="test")
        group.users.add(user)
        group.users.add(user2)
        self.assertEqual(group.users.count(), 2)

    def test_group_model_has_many_todos(self):
        todo1 = Task.objects.create(title="test", content="test")
        todo2 = Task.objects.create(title="test2", content="test")
        group = Group.objects.create(name="test", description="test")
        GroupTodo.objects.create(group=group, todo=todo1)
        GroupTodo.objects.create(group=group, todo=todo2)
        self.assertEqual(group.todos.count(), 2)
