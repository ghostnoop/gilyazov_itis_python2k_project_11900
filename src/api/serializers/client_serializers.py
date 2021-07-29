from rest_framework import serializers
from rest_framework.response import Response

from core.models import User, Client
from core.serializers.city_serializers import CitySerializer
from core.serializers.country_serializers import CountrySerializer
from core.serializers.user_serializer import UserSerializer
from rest_framework.authtoken.models import Token


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    country = CountrySerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Client
        fields = (
            "avatar",
            "religion",
            "sex",
            "country",
            "city",
            "full_name",
            "email",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}

    def create(self, validated_data: dict):
        user = self.get_user(
            validated_data.pop("email"), validated_data.pop("password")
        )
        client = Client.objects.create(user=user, **validated_data)
        return client

    def get_user(self, email, password):
        user = UserSerializer(data={"email": email, "password": password})
        if user.is_valid():
            new_user = user.save()
            return new_user


class ClientPublicSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ("user", "sex", "religion")
