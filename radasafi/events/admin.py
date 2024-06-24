from typing import Any

from django.contrib import admin
from django.http import HttpRequest

from .models import Category
from .models import Event
from .models import Location


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

    def get_prepopulated_fields(
        self,
        request: HttpRequest,
        obj: Any | None = ...,
    ) -> dict[str, tuple[str]]:
        return {"slug": ("name",)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["from_latitude", "to_latitude", "from_longitude", "to_longitude"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "general_location", "created", "updated"]
    list_filter = ["published", "created", "updated"]
    list_editable = ["published"]

    def get_prepopulated_fields(
        self,
        request: HttpRequest,
        obj: Any | None = ...,
    ) -> dict[str, tuple[str]]:
        return {"slug": ("title",)}
