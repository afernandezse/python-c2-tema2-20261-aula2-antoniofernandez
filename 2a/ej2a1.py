"""
Enunciado:
Renderiza un saludo con {{ nombre }} y calcula {{ precio * cantidad }}.
Completa renderizar_compra para devolver HTML con el nombre y el total.
Usa Environment con autoescape para que los datos no se interpreten como HTML.
"""

from jinja2 import Environment, Template


def renderizar_compra(nombre, precio, cantidad):
    """Devuelve el saludo y el importe de la compra."""

    env = Environment(autoescape=True)

    plantilla = env.from_string(
        "<h1>Hola, {{ nombre }}</h1>"
        "<p>Total: {{ precio * cantidad }} €</p>"
    )

    return plantilla.render(
        nombre=nombre,
        precio=precio,
        cantidad=cantidad
    )


if __name__ == "__main__":
    print(renderizar_compra("Ana", 12, 3))
