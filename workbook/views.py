from rest_framework import viewsets

from TodoWebsite.permissions import IsAuthenticatedAndVerified
from workbook.models import Workbook
from workbook.serializers import WorkbookSerializer


class WorkbookViewSet(viewsets.ModelViewSet):
    queryset = Workbook.objects.all()
    serializer_class = WorkbookSerializer
    permission_classes = [IsAuthenticatedAndVerified]

    def get_queryset(self):
        return self.request.user.workbooks.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, users=[self.request.user])
