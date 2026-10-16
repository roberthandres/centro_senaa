from django.db import models


class Sede(models.Model):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"


class AmbienteFormacion(models.Model):
    codigo_aula = models.CharField(
        max_length=20,
        unique=True
    )
    capacidad_maxima = models.PositiveIntegerField()

    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
        related_name="ambientes"
    )

    def __str__(self):
        return self.codigo_aula

    class Meta:
        verbose_name = "Ambiente de formación"
        verbose_name_plural = "Ambientes de formación"


class Instructor(models.Model):
    documento_identidad = models.CharField(
        max_length=20,
        primary_key=True
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo_institucional = models.EmailField(unique=True)

    ambientes = models.ManyToManyField(
        AmbienteFormacion,
        related_name="instructores",
        blank=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"