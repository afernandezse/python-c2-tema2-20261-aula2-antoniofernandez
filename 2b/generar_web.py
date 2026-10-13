"""Enunciado: Completa el generador HTML siguiendo las instrucciones de ej2b2.

Lee el JSON y renderiza la plantilla elegida con crear_entorno antes de
crear la carpeta de salida y escribir el HTML en UTF-8. Devuelve un Path.
Conserva los valores por defecto relativos al script y propaga los errores.
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
    """Lee JSON, renderiza la plantilla elegida y escribe el resultado en UTF-8."""
    # TODO: Lee los datos, renderiza la plantilla y escribe el archivo de salida.
    raise NotImplementedError("TODO: implementar generar_web")


if __name__ == "__main__":
    print(generar_web())
