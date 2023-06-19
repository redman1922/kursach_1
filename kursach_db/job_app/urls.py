from django.urls import path
from .views import (
    VacancyListView,
    VacancyDetailView,
    CompanyDetailView,
    get_pdf_1,
    get_pdf_2,
    get_pdf_3,
)

app_name = "job"

urlpatterns = [
    path('', VacancyListView.as_view(), name="vacancy_list"),
    path('<int:pk>/', VacancyDetailView.as_view(), name="vacancy_detail"),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name="company_detail"),
    path('pdf_1/', get_pdf_1, name='get-pdf-1'),
    path('pdf_2/', get_pdf_2, name='get-pdf-2'),
    path('pdf_3/', get_pdf_3, name='get-pdf-2'),
]
