from rest_framework import routers
from backend.viewsets import *

router = routers.DefaultRouter()

router.register('article', ArticleViewSet)
router.register('user', UserViewSet)
