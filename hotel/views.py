from django.shortcuts import render

from .models import Reserva


def lista_reservas(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas': reservas,
        'total_reservas': reservas.count(),
    }
    return render(request, 'hotel/lista_reservas.html', context)
