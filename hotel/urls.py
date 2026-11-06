from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
]
