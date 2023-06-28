from django.db import models
from django.conf import settings


class UserData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"

    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    avatar_img = models.ImageField(null=False)
    email = models.EmailField(max_length=254)
