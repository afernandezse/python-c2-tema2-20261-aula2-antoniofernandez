"""Tests para listados dinámicos."""

from ej2a3 import listar_productos


def test_orden():
    assert listar_productos(["Libro", "Lápiz"]) == (
        "<ul><li>Libro</li><li>Lápiz</li></ul>"
    )


def test_lista_vacia():
    assert listar_productos([]) == "<ul><li>Sin productos</li></ul>"


def test_escape():
    assert listar_productos(["<b>Libro</b>"]) == (
        "<ul><li>&lt;b&gt;Libro&lt;/b&gt;</li></ul>"
    )
