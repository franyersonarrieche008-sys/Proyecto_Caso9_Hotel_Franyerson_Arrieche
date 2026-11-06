# Sistema de Gestión de Reservas — Hotel / Hostal

Aplicación monolítica Django (patrón MVT) para el caso 9 de la Actividad 4.
La entidad principal es `Reserva` y contiene los campos solicitados en la guía:
huésped, número de habitación, noches y estado de confirmación.

## Preparación

Desde PowerShell, en la carpeta del proyecto:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Administración y ejecución

```powershell
python manage.py createsuperuser
python manage.py runserver
```

- Listado de reservas: <http://127.0.0.1:8000/reservas/>
- Página de inicio: <http://127.0.0.1:8000/>
- Panel administrativo: <http://127.0.0.1:8000/admin/>

La base de datos entregada contiene cinco reservas demostrativas. En el panel
puedes revisarlas, modificarlas o agregar otras para las evidencias del trabajo.
Si creas una base de datos nueva, ingresa al menos cinco reservas desde el panel.
El modelo valida que el número de habitación y las noches sean mayores que cero.

## Pruebas

```powershell
python manage.py test hotel
```

Para un despliegue, define `DJANGO_SECRET_KEY` en el entorno y configura
`DEBUG=False` y `ALLOWED_HOSTS` de acuerdo con el servidor.
