from django.contrib import admin
from .models import Api


@admin.register(Api)
class AdminThing(admin.ModelAdmin):

    list_display= ["title","timestamp", "updated"]