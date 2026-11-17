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

    if not isinstance(ruta, str) or not ruta:
        raise ValueError("La ruta debe ser un texto no vacío.")

    if not texto:
        raise ValueError("El texto alternativo no puede estar vacío.")

    ruta_posix = PurePosixPath(ruta)
    nombre = ruta.rsplit("/", maxsplit=1)[-1]
    if (
        ruta_posix.is_absolute()
        or not ruta_posix.name
        or nombre in {"", ".", ".."}
        or ".." in ruta
        or any(caracter.isspace() for caracter in ruta)
        or any(caracter in ruta for caracter in "\\:()")
    ):
        raise ValueError("La ruta contiene caracteres o segmentos no permitidos.")

    if "[" in texto or "]" in texto or "\n" in texto or "\r" in texto:
        raise ValueError("El texto alternativo no debe contener corchetes ni saltos de línea.")

    return f"![{texto}]({{static}}/{ruta})"


if __name__ == "__main__":
    print(imagen_estatica("images/pelican.svg", "Pelícano"))
