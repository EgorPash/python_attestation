from typing import Tuple, List, Dict
from django.db import models
from rest_framework import serializers

from electronics_store.models import NetworkMember, ContactsInfo

class ContactsInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model: models.Model = ContactsInfo
        fields: List[str] = ["email", "country", "city", "street", "house_number"]


class NetworkMemberCreateSerializer(serializers.ModelSerializer):

    supplier = serializers.SlugRelatedField(required=False, queryset=NetworkMember.objects.all(), slug_field="name")
    contacts = ContactsInfoSerializer(required=False)

    class Meta:
        model: models.Model = NetworkMember
        read_only_fields: Tuple[str, ...] = ("id", "debt", "date_of_creation")
        fields: str = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._contact: Dict[str, str] = self.initial_data.pop("contact", {})
        self.initial_data["level"] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data: dict) -> NetworkMember:
        network_member: NetworkMember = NetworkMember.objects.create(**validated_data)
        network_member.save()

        contacts: ContactsInfo = ContactsInfo.objects.create(
            base_class=network_member,
            email=self._contact.get("email", None),
            country=self._contact.get("country", None),
            city=self._contact.get("city", None),
            street=self._contact.get("street", None),
            house_number=self._contact.get("house_number", None)
            )
        contacts.save()

        return network_member


class NetworkMemberListSerializer(serializers.ModelSerializer):

    supplier = serializers.SlugRelatedField(queryset=NetworkMember.objects.all(), slug_field="name")
    contacts = ContactsInfoSerializer()

    class Meta:
        model: models.Model = NetworkMember
        fields: List[str] = ["id", "name", "level", "supplier", "debt", "contacts"]


class NetworkMemberSerializer(serializers.ModelSerializer):

    supplier = serializers.SlugRelatedField(required=False, queryset=NetworkMember.objects.all(), slug_field="name")
    contacts = ContactsInfoSerializer(required=False)

    class Meta:

        model: models.Model = NetworkMember
        fields: str = "__all__"
        read_only_fields: Tuple[str, ...] = ("id", "debt", "date_of_creation", "level")

    def is_valid(self, *, raise_exception=False):

        self._contact = self.initial_data.pop("contact", {})
        if "supplier" in self.initial_data:
            self.initial_data["level"] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):

        super().save()

        if self._contact != {}:
            self.instance.contact = self.update(self.instance.contact, self._contact)

        return self.instance


def level_detection(kwargs: dict) -> int:

    level: int = 0
    if kwargs["supplier"] is None:
        return level

    supplier: NetworkMember = NetworkMember.objects.get(name=kwargs["supplier"])

    for i in range(2):
        level += 1
        if supplier.supplier is None:
            return level
        supplier = supplier.supplier

    raise Exception("Некорректное значение в иерархической системе")
