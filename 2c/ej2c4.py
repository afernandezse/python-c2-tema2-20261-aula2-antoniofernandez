"""Enunciado: Configura la publicación en GitHub Pages de un proyecto.

Implementa una función que forme https://usuario.github.io/repositorio sin
barra final. En sitio/publishconf.py importa la configuración de desarrollo
y define SITEURL con esa URL y RELATIVE_URLS = False. Genera con
«pelican content -s publishconf.py»: no omitas el nombre del repositorio,
que es necesario para los enlaces de las páginas de proyecto.
Rechaza con ValueError usuarios vacíos o con caracteres distintos de letras
ASCII, números y guiones; el usuario debe empezar y terminar con letra o número.
El repositorio admite letras ASCII, números, guiones, puntos y guiones bajos,
pero no puede estar vacío ni ser «.» o «..».
"""

import re


def url_proyecto(usuario, repositorio):
    """Devuelve la URL HTTPS de un proyecto GitHub Pages."""
    
    if not isinstance(usuario, str) or not usuario:
        raise ValueError("El usuario debe ser un texto no vacío.")

    if not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$", usuario):
        raise ValueError("El usuario contiene caracteres no permitidos.")

    if not isinstance(repositorio, str) or not repositorio:
        raise ValueError("El repositorio debe ser un texto no vacío.")

    if repositorio in {".", ".."}:
        raise ValueError("El repositorio no puede ser '.' ni '..'.")

    if not re.match(r"^[a-zA-Z0-9._-]+$", repositorio):
        raise ValueError("El repositorio contiene caracteres no permitidos.")

    return f"https://{usuario}.github.io/{repositorio}"


if __name__ == "__main__":
    print(url_proyecto("uoc-escola-de-programacio", "python-c2-tema1-sol"))
