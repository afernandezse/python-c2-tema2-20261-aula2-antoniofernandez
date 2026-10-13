"""Enunciado: Comprueba el comando de inicialización sin ejecutar el asistente."""

from pathlib import Path
import runpy

from ej2c1 import comando_quickstart


def test_comando_quickstart():
    destino = Path(__file__).resolve().parent / "sitio"
    assert comando_quickstart(destino, "Título español", "Ana") == [
        "pelican-quickstart", "-p", str(destino),
        "-t", "Título español", "-a", "Ana", "-l", "es",
    ]


def test_destino_relativo_se_convierte_en_absoluto(monkeypatch):
    carpeta = Path(__file__).resolve().parent
    monkeypatch.chdir(carpeta)
    assert comando_quickstart("sitio")[2] == str(carpeta / "sitio")


def test_cli_destino(monkeypatch, capsys):
    archivo = Path(__file__).resolve().parent / "ej2c1.py"
    destino = archivo.parent / "otro-sitio"
    monkeypatch.setattr("sys.argv", [str(archivo), "--destino", str(destino)])
    runpy.run_path(str(archivo), run_name="__main__")
    assert f"pelican-quickstart -p {destino}" in capsys.readouterr().out
    assert not destino.exists()
