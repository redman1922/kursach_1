from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vacancy, Company


class VacancyListView(ListView):
    model = Vacancy
    template_name = "job_app/vacancy_list.html"
    context_object_name = "vacancies"


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = "job_app/vacancy_detail.html"
    context_object_name = "vacancy"


class CompanyDetailView(DetailView):
    model = Company
    template_name = "job_app/company_detail.html"
    context_object_name = "company"
