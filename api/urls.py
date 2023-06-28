from .views import SimpleUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients/create', SimpleUserViewSet, basename='userdata')
urlpatterns = router.urls
