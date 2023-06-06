from django.contrib import admin
from .models import Movie, Actor


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "date_released"]

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "bio"]