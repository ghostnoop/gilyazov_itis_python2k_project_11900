from rest_framework import serializers

from core.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")
        extra_kwargs = {"id": {"read_only": True}}
