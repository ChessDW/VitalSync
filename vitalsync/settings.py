from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-vitalsync-dev-key-change-in-production'

DEBUG = True

# Permite peticiones desde el HTML abierto localmente o desde un servidor
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'corsheaders',
    'cedulas_proxy',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # ← debe ir primero
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'vitalsync.urls'

# ── CORS ──────────────────────────────────────────────────
# Permite que el HTML (abierto como archivo o desde otro origen) llame al backend
CORS_ALLOW_ALL_ORIGINS = True

# ── CACHE (para no spamear el API de Hacienda) ────────────
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 60 * 60 * 24 * 7,  # 7 días, igual que el API original
    }
}

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [BASE_DIR / 'templates'], 'APP_DIRS': True, 'OPTIONS': {'context_processors': []}}]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'