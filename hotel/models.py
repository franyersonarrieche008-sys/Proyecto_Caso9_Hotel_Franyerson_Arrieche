from django.core.validators import MinValueValidator
from django.db import models


class Reserva(models.Model):
    nombre_huesped = models.CharField(
        max_length=100,
        verbose_name='Nombre del(la) huésped',
    )
    numero_habitacion = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Número de la habitación',
    )
    noches = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Cantidad de noches',
    )
    confirmada = models.BooleanField(
        default=False,
        verbose_name='Reserva confirmada',
    )

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ('numero_habitacion', 'nombre_huesped')

    def __str__(self):
        return f'{self.nombre_huesped} - Habitación {self.numero_habitacion}'
