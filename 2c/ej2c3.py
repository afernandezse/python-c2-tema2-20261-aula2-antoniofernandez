"""Enunciado: Incluye un recurso estático en un artículo.

Implementa una función que genere una imagen Markdown con {static}, usando
una ruta relativa a content. Añade images/pelican.svg a STATIC_PATHS mediante
la carpeta «images» en pelicanconf.py y referencia el SVG desde el artículo.
Pelican sustituirá {static} por la URL correcta al generar el sitio.
Rechaza con ValueError las rutas vacías, absolutas, sin nombre, con «..»,
espacios, tabulaciones, saltos de línea, barras inversas, dos puntos o
paréntesis. El texto alternativo no debe tener corchetes ni saltos de línea.
"""

from pathlib import PurePosixPath


def imagen_estatica(ruta, texto="Ilustración"):
    """Construye una imagen Markdown a partir de una ruta local sencilla."""
    # TODO: Valida la ruta y el texto y devuelve la referencia Markdown estática.
    raise NotImplementedError("TODO: implementar imagen_estatica")


if __name__ == "__main__":
    print(imagen_estatica("images/pelican.svg", "Pelícano"))
