from django.db import models
from common.models import CommonModel


# Create your models here.
class Experience(CommonModel):
    # Experience Model Definition

    country = models.CharField(
        max_length=150,
        default="",
    )
    city = models.CharField(
        max_length=150,
        default="",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=150,
        default="",
    )
    description = models.TextField()
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    # What is included in an experience
    name = models.CharField(
        max_length=100,
        default="",
    )
    detail = models.CharField(
        max_length=250,
        default="",
        blank=True,
    )
    explanation = models.TextField(
        default="",
        blank=True,
    )

    def __str__(self):
        return self.name
