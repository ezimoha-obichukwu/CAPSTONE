from django.contrib import admin
from .models import Movie


# Register your models here.
@admin.register(Movie)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "date_released"]