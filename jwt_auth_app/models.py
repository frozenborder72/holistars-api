from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class HoliUser(AbstractUser):
    image = models.CharField(max_length=300)
    bio = models.CharField(max_length=1000)
