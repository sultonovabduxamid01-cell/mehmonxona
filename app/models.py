from django.db import models

# Create your models here.


class Mehmonxona(models.Model):
    nomi = models.CharField(max_length=150)

    manzil = models.CharField(max_length=255)

    malumot = models.TextField()

    yulduz_soni = models.PositiveIntegerField(default=5)

    xona_soni = models.PositiveIntegerField()

    bir_kunlik_narx = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    wifi_bormi = models.BooleanField(default=True)

    emaili = models.EmailField()

    ochilgan_sana = models.DateTimeField()

    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)

    yangilangan_vaqt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomi