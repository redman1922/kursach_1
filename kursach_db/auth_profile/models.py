from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"

    last_name = models.CharField(max_length=20, null=False, db_index=True)
    first_name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(default=0)
    # city = models.ForeignKey(City)
    reg_date = models.DateTimeField(auto_created=False)
    # post = models.ForeignKey(Post)

    def __str__(self):
        return f"Employee {self.pk} {self.last_name} {self.first_name}"


class Professions(models.Model):
    class Meta:
        verbose_name = "профессия"
        verbose_name_plural = "профессии"

    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name}"


def profile_picture_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/picture/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20, null=False, db_index=True)
    first_name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(default=0)
    passport = models.CharField(max_length=20, null=False)
    passport_region = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to=profile_picture_directory_path)
    study_type = models.CharField(max_length=30, null=True, blank=True)
    study_place = models.CharField(max_length=100, null=True, blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    registrar = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="registrar", null=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    experience = models.BooleanField(default=False)
    payment = models.DecimalField(default=0, max_digits=100, decimal_places=2, null=False, blank=True)
    archived = models.BooleanField(default=False)
    archivist = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="archivist", null=True)
    professions = models.ManyToManyField(Professions, related_name="profile", null=True, blank=True)

    def __str__(self):
        return f"Profile ({self.pk}) {self.user.first_name} {self.user.last_name}"
