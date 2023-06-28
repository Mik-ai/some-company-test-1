from rest_framework import viewsets
from rest_framework import permissions

from .models import UserData
from .serializers import UserSerializer


class SimpleUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserData.objects.all()
    permission_classes = [permissions.IsAuthenticated]