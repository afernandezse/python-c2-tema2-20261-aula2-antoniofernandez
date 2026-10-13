"""Enunciado: Inicializa un sitio con pelican-quickstart.

Implementa una función que construya el comando con la carpeta de destino,
el título, el autor y el idioma español. No ejecutes el asistente desde la
función: el alumno debe ejecutarlo y responder sus preguntas en la terminal.
"""

from pathlib import Path


def comando_quickstart(destino, titulo="Mi sitio con Pelican", autor="Estudiante UOC"):
    """Devuelve los argumentos del asistente, con un destino absoluto."""
    # TODO: Devuelve los argumentos del asistente sin ejecutarlo.
    raise NotImplementedError("TODO: implementar comando_quickstart")


if __name__ == "__main__":
    import argparse
    import shlex

    parser = argparse.ArgumentParser(description="Mostrar el comando pelican-quickstart")
    parser.add_argument(
        "--destino", type=Path, default=Path(__file__).resolve().parent / "sitio",
        help="Carpeta del nuevo sitio; solo se muestra el comando",
    )
    argumentos = parser.parse_args()
    print(shlex.join(comando_quickstart(argumentos.destino)))
