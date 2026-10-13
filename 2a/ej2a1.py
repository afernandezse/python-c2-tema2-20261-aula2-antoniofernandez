"""
Enunciado:
Renderiza un saludo con {{ nombre }} y calcula {{ precio * cantidad }}.
Completa renderizar_compra para devolver HTML con el nombre y el total.
Usa Environment con autoescape para que los datos no se interpreten como HTML.
"""

from jinja2 import Environment


def renderizar_compra(nombre, precio, cantidad):
    """Devuelve el saludo y el importe de la compra."""
    # TODO: Crea y renderiza la plantilla del saludo y el total con autoescape.
    raise NotImplementedError("TODO: implementar renderizar_compra")


if __name__ == "__main__":
    print(renderizar_compra("Ana", 12, 3))
