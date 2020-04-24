from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    handle = models.CharField(max_length=16)