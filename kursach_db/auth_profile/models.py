from django.contrib.auth.models import User
from django.db import models


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


def profile_picture_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/picture/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
    class Meta:
        ordering = ["-pk"]
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20, null=False, db_index=True)
    first_name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(default=0)
    # city = models.ForeignKey(City)
    passport = models.CharField(max_length=20, null=False)
    passport_region = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to=profile_picture_directory_path)
    study_type = models.CharField(max_length=30, null=True, blank=True)
    study_place = models.CharField(max_length=100, null=True, blank=True)
    reg_date = models.DateTimeField(auto_created=False)
    registrar = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="registrar")
    # фамилия регистрирующего
    comment = models.TextField(max_length=500, null=True, blank=True)
    last_update = models.DateTimeField(auto_created=True)
    # фамилия удалившего в архив
    experience = models.BooleanField(null=False)
    payment = models.DecimalField(max_digits=100, decimal_places=2, null=False, blank=True)
    archived = models.BooleanField(default=False)
    archivist = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="archivist")

    def __str__(self):
        return f"Profile ({self.pk}) {self.last_name} {self.first_name}"
