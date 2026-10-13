"""Enunciado: Comprueba las referencias estáticas y rechaza rutas inválidas."""

import pytest

from ej2c3 import imagen_estatica


def test_imagen_estatica():
    assert imagen_estatica("images/pelican.svg", "Pelícano") == (
        "![Pelícano]({static}/images/pelican.svg)"
    )


@pytest.mark.parametrize("ruta", ["", ".", "/images/a.svg", "../a.svg", "images/../a.svg",
                                      "https://otro/a.svg", "images/a b.svg"])
def test_rechaza_rutas_invalidas(ruta):
    with pytest.raises(ValueError):
        imagen_estatica(ruta)


def test_rechaza_texto_multilinea():
    with pytest.raises(ValueError):
        imagen_estatica("images/a.svg", "Una\nimagen")
