import io

from django.shortcuts import render
from django.http import FileResponse
from django.views.generic import ListView, DetailView
from .models import Vacancy, Company
from auth_profile.models import Profile, Professions
from django.db.models import Sum, Count

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4


def get_pdf_1(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8'))

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)
    # p.setFont('DejaVuSerif', 32)

    textobj = p.beginText()
    textobj.setTextOrigin(10, 700)
    textobj.setFont('DejaVuSerif', 14)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    lines = []

    lines.append(str(Company.objects.all().count()) + " компаний.")
    lines.append(str(Vacancy.objects.all().count()) + " вакансий.")
    lines.append("Ищут работу " + str(Profile.objects.filter(archived=False).count()) + " человек(a).")
    lines.append("Не ищут работу " + str(Profile.objects.filter(archived=True).count()) + " человек(a).")
    lines.append("Кол-во искомых профессий:")
    for i in range(Professions.objects.all().count()):
        try:
            profession = Professions.objects.get(id=i)
            lines.append(str(Profile.objects.filter(professions=i).count()) + " " + profession.name)
        except:
            pass

    for line in lines:
        textobj.textLine(line)

    p.drawText(textobj)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='ticket.pdf')


def get_pdf_2(request):
    # Create a file-like buffer to receive PDF data.
    buffer_1 = io.BytesIO()
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8'))

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer_1, pagesize=A4)
    # p.setFont('DejaVuSerif', 32)

    textobj = p.beginText()
    textobj.setTextOrigin(10, 700)
    textobj.setFont('DejaVuSerif', 14)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    lines = []

    lines.append("Компании:")

    for company in Company.objects.all():
        lines.append(company.name)
        lines.append("Вакансии:")
        for vacancy in company.vacancy.all():
            lines.append(vacancy.title)

    for line in lines:
        textobj.textLine(line)

    p.drawText(textobj)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer_1.seek(0)
    return FileResponse(buffer_1, as_attachment=True, filename='companies.pdf')


def get_pdf_3(request):
    # Create a file-like buffer to receive PDF data.
    buffer_1 = io.BytesIO()
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf', 'UTF-8'))

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer_1, pagesize=A4)
    # p.setFont('DejaVuSerif', 32)

    textobj = p.beginText()
    textobj.setTextOrigin(10, 700)
    textobj.setFont('DejaVuSerif', 14)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    lines = []

    for user in Profile.objects.all():
        if user.archived:
            lines.append("Имя: " + user.first_name + " Фамилия:" + user.last_name + " не ищет работу")
        else:
            lines.append("Имя: " + user.first_name + " Фамилия:" + user.last_name + " ищет работу")

    for line in lines:
        textobj.textLine(line)

    p.drawText(textobj)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer_1.seek(0)
    return FileResponse(buffer_1, as_attachment=True, filename='companies.pdf')


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



