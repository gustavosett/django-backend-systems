from django.urls import path
from .views import UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('user', UserViewSet)