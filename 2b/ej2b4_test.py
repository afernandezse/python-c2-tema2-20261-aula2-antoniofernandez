"""Tests para macros reutilizables."""

from ej2b4 import generar_catalogo, renderizar_tarjetas


def test_macro_reutilizada():
    html = renderizar_tarjetas([
        {"nombre": "Python", "descripcion": "Plantillas"},
        {"nombre": "HTML", "descripcion": "Estructura"},
    ])
    assert html.count("<article>") == 2
    assert "<h2>Python</h2><p>Plantillas</p>" in html
    assert "<h2>HTML</h2><p>Estructura</p>" in html


def test_sin_cursos():
    html = renderizar_tarjetas([])
    assert "<!DOCTYPE html>" in html
    assert "<p>No hay cursos disponibles</p>" in html
    assert "<article>" not in html


def test_escape_macro():
    html = renderizar_tarjetas([{"nombre": "<b>", "descripcion": "<script>"}])
    assert "<h2>&lt;b&gt;</h2><p>&lt;script&gt;</p>" in html


def test_pagina_completa_con_herencia():
    html = renderizar_tarjetas([], titulo="Catálogo <b>")
    assert '<html lang="es">' in html
    assert "<header>Escuela de Programación</header>" in html
    assert "<title>Catálogo &lt;b&gt;</title>" in html
    assert "<h1>Catálogo &lt;b&gt;</h1>" in html


def test_generar_catalogo_desde_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    fuente = tmp_path / "datos.json"
    fuente.write_text(
        '{"titulo": "Catálogo", "cursos": [{"nombre": "<b>", '
        '"descripcion": "Plantillas"}]}', encoding="utf-8"
    )
    destino = tmp_path / "output" / "catalogo.html"
    assert generar_catalogo(fuente, destino) == destino
    html = destino.read_text(encoding="utf-8")
    assert "<title>Catálogo</title>" in html
    assert "<header>Escuela de Programación</header>" in html
    assert "<h2>&lt;b&gt;</h2><p>Plantillas</p>" in html


def test_generar_con_datos_del_sitio(tmp_path):
    destino = generar_catalogo(destino=tmp_path / "catalogo.html")
    html = destino.read_text(encoding="utf-8")
    assert "<title>Cursos de programación</title>" in html
    assert html.count("<article>") == 2
