from rest_framework import routers

from workbook import views

app_name = 'workbook'
router = routers.DefaultRouter()
router.register(r'workbook', views.WorkbookViewSet, basename='workbook')

urlpatterns = router.urls
