from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, validate_email
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18), ])
    email = models.EmailField(unique=True, validators=[validate_email, ])

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.pk])

