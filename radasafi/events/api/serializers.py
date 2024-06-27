from rest_framework import serializers

from radasafi.events.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name"]
        model = Category
