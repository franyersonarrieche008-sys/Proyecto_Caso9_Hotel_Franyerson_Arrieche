from django.contrib import admin

from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_huesped', 'numero_habitacion', 'noches', 'confirmada')
    search_fields = ('nombre_huesped',)
    list_filter = ('confirmada',)
    list_per_page = 25
