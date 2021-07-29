from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        return User.objects.create_user(email, password)
