from django.contrib import admin

from .models import Professions, Profile


@admin.register(Professions)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]\



@admin.register(Profile)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["pk", "last_name", "first_name"]
    list_display_links = ["pk", "last_name", "first_name"]
