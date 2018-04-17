from rest_framework import routers
from backend.viewsets import ArticleViewSet

router = routers.DefaultRouter()

router.register('article', ArticleViewSet)
