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

    # Validar metadatos
    if not all(
        isinstance(m, str) and m.strip() and "\n" not in m and "\r" not in m
        for m in [titulo, fecha, slug, categoria]
    ):
        raise ValueError("Los metadatos deben ser líneas no vacías sin saltos de línea.")
    
    # Validar fecha ISO
    try:
        date.fromisoformat(fecha)
    except ValueError:
        raise ValueError("La fecha debe ser ISO válida (YYYY-MM-DD).")
    
    # Construir el artículo
    metadatos = f"Title: {titulo}\nDate: {fecha}\nCategory: {categoria}\nSlug: {slug}\n"
    return f"{metadatos}\n{contenido.rstrip()}\n"


if __name__ == "__main__":
    print(crear_articulo(
        "Bienvenidos a Pelican", "2026-01-15", "bienvenida",
        "# Hola, mundo\n\nEste sitio está generado con Python.",
    ))
