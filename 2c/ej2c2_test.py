"""Enunciado: Comprueba las cabeceras Markdown y rechaza metadatos inválidos."""

import pytest

from ej2c2 import crear_articulo


def test_articulo_sin_delimitadores_yaml():
    assert crear_articulo("Hola", "2026-01-15", "hola", "# Hola\n", "Web") == (
        "Title: Hola\nDate: 2026-01-15\nCategory: Web\nSlug: hola\n\n# Hola\n"
    )


@pytest.mark.parametrize("fecha", ["no-es-fecha", "2026-02-30"])
def test_fecha_invalida(fecha):
    with pytest.raises(ValueError):
        crear_articulo("Hola", fecha, "hola", "Texto")


@pytest.mark.parametrize("titulo", ["", "Hola\nSlug: otro", "Hola\rDate: otra"])
def test_metadatos_invalidos(titulo):
    with pytest.raises(ValueError):
        crear_articulo(titulo, "2026-01-15", "hola", "Texto")
