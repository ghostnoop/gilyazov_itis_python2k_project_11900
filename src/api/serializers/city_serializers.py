from rest_framework import serializers

from core.models import Country, City
from core.serializers.country_serializers import CountrySerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")
        extra_kwargs = {"id": {"read_only": True}}
