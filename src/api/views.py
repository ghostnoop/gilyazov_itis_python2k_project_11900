from django.shortcuts import get_object_or_404
from rest_framework import status, authentication, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Point, Client
from core.permissions import IsOwner
from core.serializers import ClientSerializer
from core.serializers.point_serializers import PointSerializer
from core.services.services import (
    create_token,
    get_points_which_start_with,
    register_client,
)
from core.tasks import get_emails


@api_view(["POST"])
def client_register(request):
    serializer = ClientSerializer(data=request.data, required=False)

    if serializer.is_valid():
        token = register_client(serializer)
        if not token:
            return Response(
                {"message": "A user already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"token": token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def client_login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    token = get_object_or_404(Token, user__email=email)
    if token.user.check_password(password):
        return Response(
            {"token": token.key, "client": ClientSerializer(token.user.client).data}
        )
    else:
        return Response({"Password is not correct"}, status=403)


@api_view(["GET"])
def point_finder(request, name: str):
    serializer = PointSerializer(get_points_which_start_with(name))
    return Response(serializer.data)


@api_view(['GET'])
def email_getter(request):
    get_emails.delay()
    return Response({'status': 'In progress'}, status=status.HTTP_202_ACCEPTED)


class PointView(viewsets.ModelViewSet):
    serializer_class = PointSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        qs = Point.objects.select_related("client")
        if user.is_authenticated:
            qs = qs.filter(client__user=user)
        return qs

    def list(self, request, *args, **kwargs):
        """get points"""
        return super(PointView, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """get point"""
        return super(PointView, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """update point"""
        return super(PointView, self).update(request, *args, **kwargs)

    def perform_create(self, serializer):
        """create point"""
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """delete point"""
        return super(PointView, self).destroy(request, *args, **kwargs)
