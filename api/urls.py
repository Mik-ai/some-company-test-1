from .views import SimpleUserViewSet, FollowUser, UserList
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'clients/create', SimpleUserViewSet, basename='userdata')
router.register(r'clients/match', FollowUser, basename='followuser')

urlpatterns = [
    path("clients/list", UserList.as_view(), name="product-list"),
]

urlpatterns += router.urls
