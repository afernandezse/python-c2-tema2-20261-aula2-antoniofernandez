"""
Enunciado:
Completa crear_entorno para configurar Environment y FileSystemLoader.
Recibe la carpeta de plantillas y activa autoescape para HTML y XML.
Comprueba que get_template puede cargar index.html desde esa carpeta.
No cambies el directorio de trabajo para localizar las plantillas.
"""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


def crear_entorno(carpeta_plantillas):
    """Crea el entorno para cargar plantillas desde el sistema de archivos."""
    # TODO: Configura el cargador de archivos y el autoescape para HTML y XML.
    raise NotImplementedError("TODO: implementar crear_entorno")


if __name__ == "__main__":
    entorno = crear_entorno(Path(__file__).parent / "templates")
    print(entorno.get_template("index.html").render(titulo="Cursos", cursos=[]))
