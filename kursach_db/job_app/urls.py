from django.urls import path
from .views import (
    VacancyListView,
    VacancyDetailView,
    CompanyDetailView,
)

app_name = "vacancy"

urlpatterns = [
    path('', VacancyListView.as_view(), name="vacancy_list"),
    path('<int:pk>/', VacancyDetailView.as_view(), name="vacancy_detail"),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name="company_detail"),
]
