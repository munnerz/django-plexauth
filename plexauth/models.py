from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class PlexUser(AbstractUser):
    token = models.CharField(max_length=32)
    REQUIRED_FIELDS = ['token']
