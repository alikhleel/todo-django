from django.contrib.auth import get_user_model
from django.test import TestCase

from todo.models import Task
from workbook.models import Workbook, WorkbookTodo

User = get_user_model()


class WorkbookTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="example@example.com", password="test123")

    def test_group_model_has_many_users(self):
        user = self.user
        user2 = User.objects.create_user(email="example1@example.com", password="test456")
        group = Workbook.objects.create(name="test", description="test", owner=user)
        group.users.add(user)
        group.users.add(user2)
        self.assertEqual(group.users.count(), 2)

    def test_group_model_has_many_todos(self):
        user = self.user
        todo1 = Task.objects.create(title="test", content="test")
        todo2 = Task.objects.create(title="test2", content="test")
        group = Workbook.objects.create(name="test", description="test", owner=user)
        WorkbookTodo.objects.create(group=group, todo=todo1)
        WorkbookTodo.objects.create(group=group, todo=todo2)
        self.assertEqual(group.todos.count(), 2)
