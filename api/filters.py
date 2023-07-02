from django_filters.rest_framework import (
    ChoiceFilter,
    DjangoFilterBackend,
    NumberFilter,
    FilterSet,
    CharFilter,
)

GenderChoices = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class MyBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)

        # merge filterset kwargs provided by view class
        if hasattr(view, "passing_context"):
            kwargs.update(view.passing_context())

        return kwargs


class UserDataFilterSet(FilterSet):
    name = CharFilter()
    surname = CharFilter()
    gender = ChoiceFilter(choices=GenderChoices)
    distance = NumberFilter(method="distance_filter", lookup_expr="some")

    def __init__(self, *args, active_user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.active_user = active_user

    def distance_filter(self, queryset, *args, **kwargs):
        distance = self.data.get("distance")
        distance = float(distance)

        filtered_ids = [
            x.id for x in queryset if self.active_user.distance_to(x) < distance
        ]
        queryset = queryset.filter(id__in=filtered_ids)

        return queryset
