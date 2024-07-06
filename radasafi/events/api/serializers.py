from rest_framework import serializers

from radasafi.events.models import Category
from radasafi.events.models import Event
from radasafi.events.models import Location


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Location


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
