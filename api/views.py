from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend, NumberFilter

from .filters import UserDataFilterSet
from .models import UserData
from .serializers import UserSerializer, FollowUserSerializer, UserAllfieldsSerializer


from .tasks import follow_collision_email


class SimpleUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserData.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class FollowUser(viewsets.ViewSet):
    serializer_class = FollowUserSerializer
    queryset = UserData.objects.all()

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        return UserData.objects.get(pk=pk)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        follow = request.data.get("follow")
        # todo - удалить дебаг...
        print(f"{instance.id} - {follow}")

        # существует ли пользователь на которого подписываемся?
        if not UserData.objects.filter(id=follow).exists():
            return Response(
                {"discription": "user are not found"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # есть ли уже подписка на этого пользователя?
        if instance.follow.filter(pk=follow).exists():
            return Response(
                {"discription": "you are already following this user"},
                status=status.HTTP_200_OK,
            )

        # подписаться
        instance.follow.add(follow)
        u2 = UserData.objects.get(pk=follow)

        # взаимно?
        if UserData.objects.filter(follow__in=[instance.id], pk=follow).exists():
            follow_collision_email(instance.id, u2.id)

        return Response(
            {"discription": f"you are now following - {u2.name}"},
            status=status.HTTP_200_OK,
        )


class UserList(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserAllfieldsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserDataFilterSet
    exclude = ["id"]

    # distance = NumberFilter(method="distance_filter")
    # def distance_filter(self, distance):
    #     user = self.context["request"].user
    #     user = UserData.objects.get(user=user)
    #     queryset = UserData.objects.all()
    #     queryset = [x for x in queryset if user.distance_to(x) < distance]
    #     return queryset
