
from django.urls import path, include
from .views import first
from rest_framework import routers
from .views import BookViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('books', BookViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first', first)

]
