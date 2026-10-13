"""Tests para variables y expresiones básicas."""

from ej2a1 import renderizar_compra


def test_variables_y_expresion():
    assert renderizar_compra("Ana", 12, 3) == (
        "<h1>Hola, Ana</h1><p>Total: 36 €</p>"
    )


def test_cantidad_cero():
    assert "Total: 0 €" in renderizar_compra("Ana", 12, 0)


def test_escape_html():
    assert "&lt;script&gt;" in renderizar_compra("<script>", 1, 1)
