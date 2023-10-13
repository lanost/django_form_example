# Create your models here.
# user_management/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = 'student', _('Student')
        STAFF = 'staff', _('Staff')
        EDITOR = 'editor', _('Editor')
        ADMIN = 'admin', _('Admin')

    role = models.CharField(max_length=20, choices=Roles.choices)
    country = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
