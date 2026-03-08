# VitalSync

App web de salud que monitorea frecuencia cardíaca vía Bluetooth BLE, analiza niveles de ansiedad y conecta con servicios de emergencia. Incluye consulta de cédulas al API de Hacienda Costa Rica.

---

## Estructura del proyecto

```
vitalsync_backend/
├── manage.py
├── requirements.txt
├── templates/
│   └── vitalsync.html        ← App completa (frontend)
├── vitalsync/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── cedulas_proxy/
    ├── __init__.py
    ├── urls.py
    └── views.py
```

---

## Correr localmente (primera vez)

```bash
cd vitalsync_backend
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py runserver
```

Abre **http://localhost:8000** en Chrome o Edge.

## Desde el segundo uso

```bash
cd vitalsync_backend
venv\Scripts\activate
python manage.py runserver
```

---

## Funcionalidades

- **Bluetooth BLE** — Conecta con sensores de pulso cardíaco estándar (Heart Rate Service UUID 0x180D) en Chrome/Edge
- **Análisis de ansiedad** — Calcula nivel estimado con base en presión arterial y BPM
- **Ejercicios de respiración** — 4 técnicas animadas (4-7-8, cuadrada, diafragmática, coherencia cardíaca)
- **Emergencias** — Llamada al 911, farmacias cercanas, Uber/DiDi
- **Perfil** — Búsqueda por cédula vía API Hacienda CR, condiciones médicas, medicamentos, contactos de emergencia

---

## API de cédulas

```
GET /api/cedulas/<query>/
```

Proxy hacia apis.gometa.org con cache de 7 días para no saturar el API de Hacienda.

---

## Despliegue en producción

El backend Django debe desplegarse en un servidor con Python (Railway, Render, VPS). El frontend en templates/vitalsync.html es servido por Django directamente.