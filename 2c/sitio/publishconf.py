"""Enunciado: Adapta la configuración local a una página de proyecto de GitHub.

TODO (ej2c4): Carga las constantes de pelicanconf.py desde la carpeta de este
archivo, no desde el directorio del terminal, y conserva AUTHOR y SITENAME.
Define SITEURL como la URL HTTPS de tu usuario y repositorio sin barra final,
y desactiva RELATIVE_URLS. Las pruebas usan los identificadores del repositorio
del curso (uoc-escola-de-programacio y python-c2-tema1-sol); antes de publicar,
sustitúyelos por los de tu proyecto.
Configura los feeds de producción FEED_ALL_ATOM y CATEGORY_FEED_ATOM y decide
si DELETE_OUTPUT_DIRECTORY debe limpiar la salida. Revisa la ruta de salida
antes de activar su borrado. No publiques hasta completar y revisar el sitio.
"""

from pathlib import Path
import runpy

_desarrollo = runpy.run_path(str(Path(__file__).resolve().with_name("pelicanconf.py")))
globals().update(
    {nombre: valor for nombre, valor in _desarrollo.items() if not nombre.startswith("__")}
)

SITEURL = "https://uoc-escola-de-programacio.github.io/python-c2-tema1-sol"
RELATIVE_URLS = False
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
DELETE_OUTPUT_DIRECTORY = False
