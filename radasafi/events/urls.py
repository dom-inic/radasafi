from django.urls import path

from .api.views import CategoryList
from .api.views import EventList

app_name = "events"

urlpatterns = [
    path("", EventList.as_view(), name="event-list"),
    path("categories/", CategoryList.as_view(), name="category-list"),
]
