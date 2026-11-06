from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Reserva


class ListaReservasTests(TestCase):
    def test_lista_muestra_estado_vacio(self):
        response = self.client.get(reverse('lista_reservas'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aún no hay reservas registradas')
        self.assertEqual(response.context['total_reservas'], 0)

    def test_lista_muestra_reservas_y_total(self):
        Reserva.objects.create(
            nombre_huesped='María Torres',
            numero_habitacion=204,
            noches=3,
            confirmada=True,
        )

        response = self.client.get(reverse('lista_reservas'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'María Torres')
        self.assertContains(response, 'Habitación 204')
        self.assertContains(response, 'Confirmada')
        self.assertEqual(response.context['total_reservas'], 1)

    def test_ruta_corta_muestra_la_misma_lista(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel/lista_reservas.html')

    def test_habitacion_y_noches_deben_ser_mayores_que_cero(self):
        reserva = Reserva(
            nombre_huesped='Huésped de prueba',
            numero_habitacion=0,
            noches=0,
        )

        with self.assertRaises(ValidationError):
            reserva.full_clean()
