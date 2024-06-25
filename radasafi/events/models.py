from django.db import models

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
    from_latitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    from_longitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    to_latitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    to_longitude = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    class Meta:
        verbose_name_plural = "locations"

    def __str__(self) -> str:
        return f"({self.from_latitude},{self.from_longitude}),({self.to_latitude}"


class Event(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category",
        verbose_name="event_category",
        on_delete=models.CASCADE,
    )

    link = models.URLField(blank=True)
    location = models.ForeignKey(
        Location,
        verbose_name="event_location",
        on_delete=models.CASCADE,
        blank=True,
    )
    general_location = models.CharField(max_length=200, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
