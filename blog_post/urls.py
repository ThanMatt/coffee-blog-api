from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'', BlogPostViewSet, basename='blog-post')

urlpatterns = [
  path('', include(router.urls)),
]
