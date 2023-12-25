from rest_framework import routers

from todo import views
app_name = 'todo'
router = routers.DefaultRouter()
router.register(r'todo', views.TaskViewSet, basename='todo')

urlpatterns = router.urls
