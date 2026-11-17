"""
Enunciado:
Después de la página con herencia de ej2b3, genera un catálogo de cursos.
Define una macro tarjeta(nombre, descripcion) en macros.html. Haz que
tarjetas.html herede de base.html e importe la macro para cada curso de
datos.json. Cada tarjeta debe ser un <article> con <h2> y <p>.
Usa titulo en <title> y <h1> y escapa los datos de todas las tarjetas.
Completa renderizar_tarjetas y generar_catalogo reutilizando crear_entorno
y generar_web. Guarda la página completa en output/catalogo.html, sin
duplicar la estructura base ni el HTML de las tarjetas.
Si no hay cursos, muestra "No hay cursos disponibles". Abre el resultado
en el navegador y comprueba que comparte la cabecera de bienvenida.html.
"""

from pathlib import Path

from ej2b1 import crear_entorno
from generar_web import CARPETA, generar_web


def renderizar_tarjetas(cursos, titulo="Cursos"):
    """Renderiza el catálogo completo mediante herencia y una macro importada."""

    carpeta_plantillas = CARPETA / "templates"
    entorno = crear_entorno(carpeta_plantillas)
    plantilla = entorno.get_template("tarjetas.html")
    html = plantilla.render(cursos=cursos, titulo=titulo)
    return html



def generar_catalogo(
    fuente=CARPETA / "datos.json",
    destino=CARPETA / "output" / "catalogo.html",
):
    """Genera el catálogo estático a partir de los datos del sitio."""
    return generar_web(
        fuente=fuente,
        carpeta_plantillas=CARPETA / "templates",
        destino=destino,
        plantilla="tarjetas.html",
    )



if __name__ == "__main__":
    print(generar_catalogo())
