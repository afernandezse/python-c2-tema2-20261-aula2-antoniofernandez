"""
Enunciado:
Completa generar_web.py para leer datos.json (UTF-8), cargar index.html
mediante crear_entorno y generar un archivo HTML estático.
Crea la carpeta de salida si no existe y devuelve la ruta del HTML.
El JSON contiene titulo y cursos (lista de objetos con nombre y descripcion).
Completa index.html: muestra titulo en <title> y <h1>, y recorre cursos
en un <ul> con <li><strong>nombre</strong>: descripcion</li>.
Si no hay cursos, muestra <li>No hay cursos disponibles</li>.
Escapa los datos y lee el JSON antes de escribir para no sobrescribir la
salida si el JSON es inválido; propaga los errores de lectura y decodificación.
El generador debe aceptar el nombre de plantilla para reutilizarlo en 2b3/2b4.
Usa rutas relativas al script para los valores por defecto, no al terminal.
Ejecuta generar_web.py y abre 2b/output/index.html en el navegador.
"""


import json
from pathlib import Path
from ej2b1 import crear_entorno


CARPETA = Path(__file__).resolve().parent


def generar_web(
    fuente=CARPETA / "datos.json",
    carpeta_plantillas=CARPETA / "templates",
    destino=CARPETA / "output" / "index.html",
    *,
    plantilla="index.html",
):
    """Genera una página HTML estática a partir de un JSON."""

    fuente = Path(fuente)
    carpeta_plantillas = Path(carpeta_plantillas)
    destino = Path(destino)

    # Leer los datos antes de modificar el archivo de salida
    with fuente.open("r", encoding="utf-8") as f:
        datos = json.load(f)

    # Preparar el entorno Jinja2
    entorno = crear_entorno(carpeta_plantillas)

    # Cargar la plantilla solicitada
    template = entorno.get_template(plantilla)

    # Renderizar utilizando todos los campos del JSON
    html = template.render(**datos)

    # Crear la carpeta de salida si no existe
    destino.parent.mkdir(parents=True, exist_ok=True)

    # Guardar el documento HTML
    destino.write_text(html, encoding="utf-8")

    return destino




if __name__ == "__main__":
    print(generar_web())
