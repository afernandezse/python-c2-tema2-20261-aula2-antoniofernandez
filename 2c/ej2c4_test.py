"""Enunciado: Comprueba la URL del proyecto y las configuraciones reales."""

from pathlib import Path
import runpy

import pytest

from ej2c4 import url_proyecto


def test_url_de_proyecto():
    assert url_proyecto("estudiante-uoc", "mi-sitio") == (
        "https://estudiante-uoc.github.io/mi-sitio"
    )


@pytest.mark.parametrize("usuario, repositorio", [
    ("", "sitio"), ("ana/otro", "sitio"), ("ana", ""), ("ana", "../sitio"),
    ("ana", ".."), ("ana", "mi sitio"),
])
def test_url_invalida(usuario, repositorio):
    with pytest.raises(ValueError):
        url_proyecto(usuario, repositorio)


def test_configuraciones_desde_otro_directorio(monkeypatch):
    sitio = Path(__file__).resolve().parent / "sitio"
    monkeypatch.chdir(sitio.parent)
    desarrollo = runpy.run_path(str(sitio / "pelicanconf.py"))
    produccion = runpy.run_path(str(sitio / "publishconf.py"))
    assert desarrollo["SITEURL"] == ""
    assert desarrollo["RELATIVE_URLS"] is True
    assert desarrollo["STATIC_PATHS"] == ["images"]
    assert Path(desarrollo["PATH"]) == sitio / "content"
    assert produccion["SITEURL"] == url_proyecto(
        "uoc-escola-de-programacio", "python-c2-tema1-sol"
    )
    assert produccion["RELATIVE_URLS"] is False
    assert produccion["AUTHOR"] == desarrollo["AUTHOR"]
