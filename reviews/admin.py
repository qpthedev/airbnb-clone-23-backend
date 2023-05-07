from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad"),
            ("good", "Good"),
            ("great", "Great"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            if word == "bad":
                return reviews.filter(rating__lte=1.5)
            elif word == "good":
                return reviews.filter(rating__gt=1.5).filter(rating__lte=3.5)
            elif word == "great":
                return reviews.filter(rating__gt=3.5)
        else:
            return reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__username",
    )
