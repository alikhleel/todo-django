# Generated by Django 5.0 on 2023-12-26 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_end_data'),
        ('workbook', '0002_group_grouptodo_delete_workbook'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupTodo',
            new_name='WorkbookTodo',
        ),
        migrations.CreateModel(
            name='Workbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_workbooks', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='workbooks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='workbooktodo',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='workbook.workbook'),
        ),
        migrations.CreateModel(
            name='WorkbookUserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_edit', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workbook_permissions', to=settings.AUTH_USER_MODEL)),
                ('workbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='workbook.workbook')),
            ],
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]