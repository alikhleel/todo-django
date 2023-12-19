from rest_framework import serializers

from todo.models import Task


class ParentTaskChoiceField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        queryset = Task.objects.filter(created_by=user)
        return queryset


class TaskSerializer(serializers.ModelSerializer):
    parent_task = ParentTaskChoiceField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'content', 'completed', 'parent_task', 'created', 'end_data']
        read_only_fields = ['id', 'created']

    def validate(self, attrs):
        if attrs.get('parent_task') and attrs.get('parent_task').parent_task:
            parent_task = attrs.get('parent_task')
            raise serializers.ValidationError({'parent_task': f'Parent task {parent_task} already has a parent task.'})
        return attrs
