"""
Enunciado:
Completa listar_productos con un bucle for de Jinja2 para crear un <ul>.
Cada nombre debe aparecer en un <li>, en el orden recibido.
Usa el else del bucle para mostrar <li>Sin productos</li> si la lista está vacía.
"""

from jinja2 import Environment


def listar_productos(productos):
    """Devuelve una lista HTML de productos."""
    # TODO: Renderiza los productos con for/else y autoescape en Jinja2.
    raise NotImplementedError("TODO: implementar listar_productos")


if __name__ == "__main__":
    print(listar_productos(["Libro", "Lápiz"]))
