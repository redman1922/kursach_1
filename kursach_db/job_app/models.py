from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=50, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True, max_length=2000, verbose_name="обязанности")
    requirements = models.TextField(null=True, blank=True, max_length=2000, verbose_name="требования")
    conditions = models.TextField(null=True, blank=True, max_length=2000, verbose_name="условия")
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Vacancy {self.title} ({self.pk})"


class Company(models.Model):
    name = models.CharField(max_length=100, null=False)
    comment = models.TextField(max_length=2000, null=True, blank=True)
    vacancies = models.ManyToManyField(Vacancy, related_name="companies", null=True)

    def __str__(self):
        return f"Company {self.name}"
