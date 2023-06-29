from .views import SimpleUserViewSet, FollowUser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients/create', SimpleUserViewSet, basename='userdata')
router.register(r'clients/match', FollowUser, basename='followuser')

urlpatterns = []

urlpatterns += router.urls
