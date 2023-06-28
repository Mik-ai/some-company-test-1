from django.db import models
from django.conf import settings

from PIL import Image
import os

WATERMARK_PATH = os.path.join(os.path.dirname(__file__), "src", "watermark.png")


class UserData(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"

    gender = models.CharField(max_length=20, choices=GenderChoices.choices)
    avatar_img = models.ImageField(null=False)
    email = models.EmailField(max_length=254)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.avatar_img.path)
        image.thumbnail((200, 200))

        crop_image = Image.open(WATERMARK_PATH)
        crop_image.thumbnail((50, 50))

        img_watermarked = image.copy()
        img_watermarked.paste(crop_image, (0, 0))

        image = img_watermarked

        image.save(self.avatar_img.path)
