from datetime import datetime

from django.db import IntegrityError
from django.db.models import Q, Max, F, Count
from rest_framework.authtoken.models import Token

from core.models import Client, Point


def register_client(serializer):
    try:
        client = serializer.save()
        token = create_token(client)
    except IntegrityError:
        return False
    return token


def create_token(client):
    token = Token.objects.create(user=client.user)
    return token.key


def get_points_which_start_with(name: str):
    return Point.objects.filter(
        Q(surname__contains=name) | Q(name__contains=name) | Q(last_name__contains=name)
    )


def get_points_which_not_dead_at_the_current_day():
    return Point.objects.exclude(birth_date=F("dead_date"))


def get_from_clients_max_count_of_points():
    return Client.objects.annotate(points=Count("point")).aggregate(
        max_count=Max("points")
    )["max_count"]


def get_emails_for_notify():
    today = datetime.now().date()
    current_date = Q(birth_date=today) | Q(dead_date=today)
    return (
        Point.objects.filter(current_date)
        .prefetch_related("client")
        .values_list("client__user__email", "name")
    )
