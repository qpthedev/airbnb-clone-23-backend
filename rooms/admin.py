from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Increase price by 5")
def increase_price_5(model_admin, request, rooms):
    for room in rooms.all():
        room.price += 5
        room.save()


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (increase_price_5,)

    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "rating",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "price",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
