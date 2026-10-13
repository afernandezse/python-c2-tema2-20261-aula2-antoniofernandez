"""Tests para herencia de plantillas."""

from ej2b3 import generar_sitio_heredado, renderizar_pagina


def test_herencia():
    html = renderizar_pagina("Inicio", "Bienvenida")
    assert '<html lang="es">' in html
    assert "<header>Escuela de Programación</header>" in html
    assert "<title>Inicio</title>" in html
    assert "<main><h1>Inicio</h1><p>Bienvenida</p></main>" in html


def test_otra_carpeta_y_escape(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    html = renderizar_pagina("<b>Inicio</b>", "<script>")
    assert "<title>&lt;b&gt;Inicio&lt;/b&gt;</title>" in html
    assert "<p>&lt;script&gt;</p>" in html


def test_generar_pagina_desde_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    fuente = tmp_path / "datos.json"
    fuente.write_text(
        '{"titulo": "Inicio", "mensaje": "Hola <b>"}', encoding="utf-8"
    )
    destino = tmp_path / "output" / "bienvenida.html"
    assert generar_sitio_heredado(fuente, destino) == destino
    html = destino.read_text(encoding="utf-8")
    assert "<!DOCTYPE html>" in html
    assert "<header>Escuela de Programación</header>" in html
    assert "<title>Inicio</title>" in html
    assert "<p>Hola &lt;b&gt;</p>" in html


def test_generar_con_datos_del_sitio(tmp_path):
    destino = generar_sitio_heredado(destino=tmp_path / "bienvenida.html")
    assert "Bienvenidos a nuestro sitio" in destino.read_text(encoding="utf-8")
