from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    favorites = models.ManyToManyField("restaurants.Restaurant", blank=True, related_name='favorited_by')

