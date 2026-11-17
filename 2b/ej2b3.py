"""
Enunciado:
Después de generar index.html en ej2b2, crea una página de bienvenida
sin duplicar la estructura del sitio. Reutiliza crear_entorno de ej2b1.
Completa base.html con los bloques titulo y contenido; en hija.html usa
extends y sobrescribe ambos bloques con titulo y mensaje de datos.json.
La base debe incluir la cabecera "Escuela de Programación"; en el bloque
contenido de la hija muestra <h1>titulo</h1><p>mensaje</p>, escapando los datos.
Completa renderizar_pagina y generar_sitio_heredado. Reutiliza generar_web
seleccionando hija.html y guarda el resultado en output/bienvenida.html.
Abre el archivo en el navegador y comprueba que conserva la cabecera común.
Las rutas deben funcionar aunque ejecutes el script desde otra carpeta.
"""

from pathlib import Path

from ej2b1 import crear_entorno
from generar_web import CARPETA, generar_web


def renderizar_pagina(titulo, mensaje):
    """Renderiza una plantilla hija conservando la estructura de la base."""
    
    carpeta_plantillas = CARPETA / "templates"
    entorno = crear_entorno(carpeta_plantillas)
    plantilla = entorno.get_template("hija.html")
    html = plantilla.render(titulo=titulo, mensaje=mensaje)
    return html



def generar_sitio_heredado(
    fuente=CARPETA / "datos.json",
    destino=CARPETA / "output" / "bienvenida.html",
):
    return generar_web(
        fuente=fuente,
        carpeta_plantillas=CARPETA / "templates",
        destino=destino,
        plantilla="hija.html",
    )


if __name__ == "__main__":
    print(generar_sitio_heredado())