from rest_framework import generics

from radasafi.events.models import Category
from radasafi.events.models import Event

from .serializers import CategorySerializer
from .serializers import EventSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
