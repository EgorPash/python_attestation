from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from typing import List
from rest_framework import permissions, serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from electronics_store.models import NetworkMember
from electronics_store.serializers import NetworkMemberCreateSerializer, NetworkMemberListSerializer, NetworkMemberSerializer


class NetworkMemberCreateView(CreateAPIView):

    model: models.Model = NetworkMember
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: serializers.ModelSerializer = NetworkMemberCreateSerializer


class NetworkMemberListView(ListAPIView):

    model: models.Model = NetworkMember
    queryset: List[NetworkMember] = NetworkMember.objects.all()
    permission_classes: list = [permissions.IsAuthenticated]
    serializer_class: serializers.ModelSerializer = NetworkMemberListSerializer
    filter_backends: list = [DjangoFilterBackend,]
    filterset_fields: List[str] = ["contactsinfo__country", ]


class NetworkMemberView(RetrieveUpdateDestroyAPIView):

    model: models.Model = NetworkMember
    queryset: List[NetworkMember] = NetworkMember.objects.all()
    serializer_class: serializers.ModelSerializer = NetworkMemberSerializer
    permission_classes: list = [permissions.IsAuthenticated,]

