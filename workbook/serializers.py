from rest_framework import serializers

from workbook.models import Workbook


class WorkbookSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Workbook
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
        }
