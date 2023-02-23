from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api-user', views.UserViewSet)

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('api/', include(router.urls)),
]
