from datetime import datetime
from factory import Faker
from faker import Faker as Fake
from django.contrib.auth import get_user_model
from django.test import TestCase
from factory.django import DjangoModelFactory
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APITestCase, CoreAPIClient, RequestsClient, APIClient

from core.models import Client, Point
from core.services.services import (
    create_token,
    get_points_which_start_with,
    get_points_which_not_dead_at_the_current_day,
    get_from_clients_max_count_of_points,
    get_emails_for_notify,
)

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Faker("email")
    password = Faker("password")


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client

    phone = Faker("random_int")
    religion = Faker("pystr")
    birth = Faker("date")
    full_name = Faker("name")


class PointFactory(DjangoModelFactory):
    class Meta:
        model = Point

    surname = Faker("first_name")
    name = Faker("name")
    last_name = Faker("last_name")
    birth_date = Faker("date")
    dead_date = Faker("date")
    latitude = Faker("pyfloat")
    longitude = Faker("pyfloat")


class ServicesTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = ClientFactory(user=self.user)
        self.point = PointFactory(client=self.client)

    def test_create_token(self):
        token = Token.objects.create(user=self.user).key
        client_new = ClientFactory(user=UserFactory())
        service = create_token(client=client_new)

        self.assertNotEqual(token, service)

    def test_find_points_by_name_found(self):
        name = self.point.name
        points = get_points_which_start_with(name)

        self.assertIn(self.point, points)

    def test_find_point_by_name_not_found(self):
        point_new = PointFactory(client=self.client)
        point_new.name = "00000"
        points = get_points_which_start_with(point_new.name)

        self.assertNotIn(point_new, points)

    def test_get_points_which_not_dead_at_the_current_day(self):
        self.point.birth_date = self.point.dead_date
        self.point.save()
        result = get_points_which_not_dead_at_the_current_day()

        self.assertEqual(len(result), 0)

    def test_get_from_clients_max_count_of_points(self):
        result = get_from_clients_max_count_of_points()

        self.assertEqual(result, 1)

    def test_get_emails_for_notify(self):
        self.point.birth_date = datetime.now().date()
        self.point.save()
        result = get_emails_for_notify()

        self.assertEqual(result[0][0], self.point.client.user.email)


class APITests(APITestCase):
    def setUp(self):
        self.api_client = APIClient()
        fake = Fake()

        self.client_data = {
            "phone": fake.random_int(),
            "email": fake.email(),
            "password": fake.password(),
            "birth": str(fake.date()),
            "full_name": fake.name(),
        }

        self.point_data = {
            "surname": fake.name(),
            "name": fake.name(),
            "last_name": fake.name(),
            "birth_date": fake.date(),
            "dead_date": fake.date(),
            "latitude": fake.pyfloat(),
            "longitude": fake.pyfloat(),
        }

        self.user = UserFactory()
        self.user.set_password(self.client_data["password"])
        self.user.save()
        self.client = ClientFactory(user=self.user)
        Token.objects.create(user=self.user)

        self.api_client.credentials(
            HTTP_AUTHORIZATION="Token " + Token.objects.first().key
        )

    def test_register_client(self):
        response: Response = self.api_client.post(
            reverse("register"), self.client_data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Token.objects.all()[1].key, response.data["token"])

    def test_login_client(self):
        data = {"email": self.user.email, "password": self.client_data["password"]}
        response: Response = self.api_client.post(reverse("login"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Token.objects.first().key, response.data["token"])

    def test_create_point(self):
        url = "/points/"
        response: Response = self.api_client.post(url, self.point_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["client"], self.client.id)

    def test_get_points(self):
        PointFactory(client=self.client)

        url = "/points/"
        response: Response = self.api_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data), Point.objects.filter(client=self.client).count()
        )

    def test_update_point(self):
        point = PointFactory(client=self.client)

        url = f"/points/{point.id}/"
        name = Fake().name()

        response: Response = self.api_client.patch(url, dict(name=name), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], name)

    def test_delete_point(self):
        point = PointFactory(client=self.client)

        url = f"/points/{point.id}/"

        response: Response = self.api_client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_point(self):
        point = PointFactory(client=self.client)

        url = f"/points/{point.id}/"
        response: Response = self.api_client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], point.id)
