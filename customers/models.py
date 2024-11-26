from django.contrib.auth.models import AbstractUser
from django.db import models

from my_project.settings import NULLABLE

class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(
        verbose_name="Электронная почта", unique=True, help_text="Введите адрес электронной почты"
    )
    phone = models.CharField(
        max_length=40,
        verbose_name="Телефонный номер",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=45, verbose_name="Город", **NULLABLE, help_text="Введите город"
    )
    avatar = models.ImageField(
        upload_to="customers/", verbose_name="Аватар", **NULLABLE, help_text="Выберите аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"
        ordering = ["-date_joined", "-email"]

    def __str__(self):
        return f"Сотрудник: {self.email}"


