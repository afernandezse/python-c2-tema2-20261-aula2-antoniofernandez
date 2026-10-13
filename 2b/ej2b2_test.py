"""Tests del generador HTML, sin escribir en la salida del repositorio."""

import json
from pathlib import Path

import pytest

from ej2b2 import generar_web


PLANTILLAS = Path(__file__).parent / "templates"


def test_generacion_json_utf8_y_escape(tmp_path):
    fuente = tmp_path / "datos.json"
    fuente.write_text(json.dumps({
        "titulo": "Programación <script>",
        "cursos": [{"nombre": "Python", "descripcion": "Diseño & HTML"}],
    }), encoding="utf-8")
    destino = tmp_path / "salida" / "index.html"
    assert generar_web(fuente, PLANTILLAS, destino) == destino
    html = destino.read_text(encoding="utf-8")
    assert "<title>Programación &lt;script&gt;</title>" in html
    assert "<strong>Python</strong>: Diseño &amp; HTML" in html


def test_lista_vacia(tmp_path):
    fuente = tmp_path / "datos.json"
    fuente.write_text('{"titulo": "Cursos", "cursos": []}', encoding="utf-8")
    destino = generar_web(fuente, PLANTILLAS, tmp_path / "index.html")
    assert "No hay cursos disponibles" in destino.read_text(encoding="utf-8")


def test_rutas_por_defecto_independientes_del_terminal(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    destino = generar_web(destino=tmp_path / "index.html")
    assert "Cursos de programación" in destino.read_text(encoding="utf-8")


def test_json_invalido_no_sobrescribe_salida(tmp_path):
    fuente = tmp_path / "datos.json"
    fuente.write_text("{", encoding="utf-8")
    destino = tmp_path / "index.html"
    destino.write_text("Anterior", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        generar_web(fuente, PLANTILLAS, destino)
    assert destino.read_text(encoding="utf-8") == "Anterior"


def test_fuente_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        generar_web(tmp_path / "ausente.json", PLANTILLAS, tmp_path / "index.html")
