"""
Enunciado:
Completa resumir_usuario aplicando los filtros upper, default y length.
Recibe un diccionario con nombre y cursos. Usa "Invitado" cuando nombre falte
o esté vacío (default con segundo argumento true), conviértelo a mayúsculas
y muestra el número de cursos. Si cursos falta, usa una lista vacía.
"""

from jinja2 import Environment


def resumir_usuario(usuario):
    """Devuelve el nombre normalizado y el número de cursos."""
    # TODO: Aplica upper, default y length en la plantilla con autoescape.
    raise NotImplementedError("TODO: implementar resumir_usuario")


if __name__ == "__main__":
    print(resumir_usuario({"nombre": "Ana", "cursos": ["Python", "HTML"]}))
