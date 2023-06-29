from django_filters.rest_framework import (
    ChoiceFilter,
    DjangoFilterBackend,
    NumberFilter,
    FilterSet,
    CharFilter,
)
from .models import UserData

GenderChoices = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class UserDataFilterSet(FilterSet):
    name = CharFilter()
    surname = CharFilter()
    gender = ChoiceFilter(choices=GenderChoices)
    id = NumberFilter(method="id_filter")
    distance = NumberFilter(method="distance_filter", lookup_expr="some")

    # when u don't have time but work should be done...
    def id_filter(self, queryset, *args, **kwargs):
        return queryset

    def distance_filter(self, queryset, *args, **kwargs):
        distance = self.data.get("distance")
        distance = float(distance)

        user = UserData.objects.get(pk=self.data.get("id"))

        filtered_ids = [x.id for x in queryset if user.distance_to(x) < distance]
        queryset = UserData.objects.filter(id__in=filtered_ids)

        return queryset
