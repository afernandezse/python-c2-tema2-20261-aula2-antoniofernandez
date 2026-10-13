"""
Enunciado:
Completa clasificar_nota usando if/elif/else dentro de una plantilla Jinja2.
Para una nota de 0 a 10, muestra "Excelente" si es >= 9, "Aprobado" si
es >= 5 y "Suspenso" en los demás casos. No decidas el resultado en Python.
"""

from jinja2 import Environment


def clasificar_nota(nota):
    """Renderiza la clasificación de una nota."""
    # TODO: Clasifica la nota con if/elif/else dentro de la plantilla.
    raise NotImplementedError("TODO: implementar clasificar_nota")


if __name__ == "__main__":
    print(clasificar_nota(7))
