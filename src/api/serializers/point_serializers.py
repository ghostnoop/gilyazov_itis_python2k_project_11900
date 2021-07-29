from rest_framework import serializers

from core.models import Point, Client


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = [
            "id",
            "client",
            "surname",
            "name",
            "last_name",
            "birth_date",
            "dead_date",
            "relation",
            "comment",
            "latitude",
            "longitude",
            "avatar",
        ]
        extra_kwargs = {"id": {"read_only": True}, "client": {"read_only": True}}

    def create(self, validated_data, *args, **kwargs):
        user = validated_data.pop("user")
        client = Client.objects.get(user=user)
        point = Point.objects.create(client=client, **validated_data)
        return point

    def update(self, instance, validated_data):

        instance: Point
        instance.surname = validated_data.get("surname", instance.surname)
        instance.name = validated_data.get("name", instance.name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.dead_date = validated_data.get("dead_date", instance.dead_date)
        instance.relation = validated_data.get("relation", instance.relation)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.latitude = validated_data.get("latitude", instance.latitude)
        instance.longitude = validated_data.get("longitude", instance.longitude)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.save()

        return instance
