from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, 'tasks')
router.register(r'categories', views.CategoryViewSet, 'categories')
router.register(r'people', views.PersonViewSet,'people')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
