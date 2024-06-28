from django.db import models
from django.utils import timezone

from radasafi.users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    latitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True)
    address = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "locations"

    def __str__(self) -> str:
        return f"({self.latitude}, {self.longitude})"


class Event(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    link = models.URLField(blank=True)
    start_location = models.ForeignKey(
        Location,
        verbose_name="event_start_location",
        on_delete=models.CASCADE,
        blank=True,
        related_name="event_start_location",
    )
    end_location = models.ForeignKey(
        Location,
        verbose_name="event_end_location",
        on_delete=models.CASCADE,
        blank=True,
        related_name="event_end_location",
    )
    published = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
