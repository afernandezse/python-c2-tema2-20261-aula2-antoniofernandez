"""Enunciado: Completa la configuración de desarrollo del sitio Pelican.

Personaliza AUTHOR y SITENAME, configura el idioma español y la zona horaria
Europe/Madrid. Conserva SITEURL vacío y los enlaces relativos en desarrollo.
PATH debe señalar content junto a este archivo desde cualquier directorio.
En ej2c3 añade la carpeta images a STATIC_PATHS para copiar el SVG.
Desactiva los feeds de desarrollo y la paginación.
"""

from pathlib import Path

AUTHOR = "Antonio Fernández"
SITENAME = "Unidad 2 - Python C2"
SITEURL = ""

PATH = str(Path(__file__).resolve().parent / "content")
STATIC_PATHS = ["images"]  # TODO (ej2c3): Incluye la carpeta de recursos estáticos.
RELATIVE_URLS = True


TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"
# AUTHOR_FEED_ATOM y AUTHOR_FEED_RSS; configura DEFAULT_PAGINATION.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
