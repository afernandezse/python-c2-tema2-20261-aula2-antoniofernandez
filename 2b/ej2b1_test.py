"""Tests para Environment y FileSystemLoader."""

import pytest
from jinja2 import FileSystemLoader, TemplateNotFound

from ej2b1 import crear_entorno


def test_loader_y_contexto(tmp_path):
    (tmp_path / "saludo.html").write_text("<h1>{{ nombre }}</h1>", encoding="utf-8")
    entorno = crear_entorno(tmp_path)
    assert isinstance(entorno.loader, FileSystemLoader)
    assert entorno.get_template("saludo.html").render(nombre="Ana") == "<h1>Ana</h1>"


@pytest.mark.parametrize("extension", ["html", "xml"])
def test_autoescape(tmp_path, extension):
    nombre = f"saludo.{extension}"
    (tmp_path / nombre).write_text("{{ texto }}", encoding="utf-8")
    assert crear_entorno(tmp_path).get_template(nombre).render(texto="<b>") == "&lt;b&gt;"


def test_plantilla_inexistente(tmp_path):
    with pytest.raises(TemplateNotFound):
        crear_entorno(tmp_path).get_template("ausente.html")
