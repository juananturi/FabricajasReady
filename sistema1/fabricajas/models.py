from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)


class Cliente(models.Model):
    nit = models.CharField(max_length=50)

    def __str__(self):
        return self.nit


class Certificado(models.Model):
    ANIOS = (
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
        # Agrega los años que necesites
    )
    anio = models.IntegerField(choices=ANIOS)
    archivo_pdf = models.FileField(upload_to='certificados/')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
