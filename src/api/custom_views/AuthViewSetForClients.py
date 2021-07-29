from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from core.models import Client


class AuthViewSetForClients(viewsets.ModelViewSet):
    def get_object(self):
        return get_object_or_404(Client, user=self.request.user)

    def get_object_by_pk(self, obj, **kwargs):
        return get_object_or_404(
            obj, pk=int(kwargs.get("pk")), creator_id=self.get_object()
        )
