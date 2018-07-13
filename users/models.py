from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.pk])

