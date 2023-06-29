from rest_framework import serializers
from api.models import UserData


class UserAllfieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"


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


class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"

    def validate(self, data):
        data["user"] = self.context["request"].user
        return data
