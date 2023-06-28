from rest_framework import serializers
from api.models import UserData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            "id",
            "name",
            "surname",
            "gender",
            "avatar_img",
            "email",
            "user",
        ]
        read_only_fields = ["user"]

    def validate(self, data):
        data["user"] = self.context["request"].user
        return data
