"""Enunciado: Escribe un artículo Markdown para Pelican.

Implementa una función que añada Title, Date, Category y Slug al principio
del texto y separe los metadatos del contenido mediante una línea vacía.
Pelican usa cabeceras «Clave: valor»: NO añadas delimitadores YAML «---».
Guarda un ejemplo en sitio/content/bienvenida.md.
Valida que los metadatos sean líneas no vacías sin saltos de línea y que
la fecha sea ISO válida; lanza ValueError si no lo son. Termina el artículo
con un único salto de línea, eliminando los espacios finales del contenido.
"""

from datetime import date


def crear_articulo(titulo, fecha, slug, contenido, categoria="Python"):
    """Devuelve Markdown con metadatos Pelican y fecha ISO válida."""
    # TODO: Valida los metadatos y construye el artículo Markdown de Pelican.
    raise NotImplementedError("TODO: implementar crear_articulo")


if __name__ == "__main__":
    print(crear_articulo(
        "Bienvenidos a Pelican", "2026-01-15", "bienvenida",
        "# Hola, mundo\n\nEste sitio está generado con Python.",
    ))
