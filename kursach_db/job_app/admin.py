from django.contrib import admin

from .models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "price"]
    list_display_links = ["pk", "title"]
    list_per_page = 20


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]
    list_per_page = 20
