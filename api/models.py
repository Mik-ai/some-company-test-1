from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"

    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    avatar_img = models.ImageField(null=False)
    email = models.EmailField(max_length=254)
