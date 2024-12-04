# mi_proyecto/asgi.py
import os
from fastapi import FastAPI
from django.core.asgi import get_asgi_application
from starlette.middleware.trustedhost import TrustedHostMiddleware

# Establecer el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')

# Crear la aplicación FastAPI
fastapi_app = FastAPI()

# Integrar rutas de FastAPI
@fastapi_app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI integrated with Django!"}

# Obtener la aplicación Django
django_app = get_asgi_application()

# Usar un Middleware para gestionar ambas aplicaciones (FastAPI y Django)
from starlette.middleware.base import BaseHTTPMiddleware

class DjangoFastAPIMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        return response

# Crear la aplicación combinada
from fastapi.middleware.cors import CORSMiddleware

app = fastapi_app

# Agregar CORS middleware si se requiere
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Agregar Django y FastAPI como middleware
app.add_middleware(DjangoFastAPIMiddleware)

# Incluir el ASGI de Django como una ruta
app.mount("/django", django_app)
