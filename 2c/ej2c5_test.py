"""Enunciado: Comprueba el despliegue simulando Pelican, ghp-import y sus fallos."""

from pathlib import Path
import runpy
import subprocess
from unittest.mock import call, patch

import pytest

from ej2c5 import SITIO, comandos_publicacion, publicar


def test_comandos_desde_cualquier_directorio(monkeypatch):
    monkeypatch.chdir(SITIO)
    generar, desplegar = comandos_publicacion()
    assert generar == [
        "pelican", str(SITIO / "content"), "-s", str(SITIO / "publishconf.py"),
        "-o", str(SITIO / "output"),
    ]
    assert desplegar == [
        "ghp-import", "-n", "-p", "-b", "gh-pages", str(SITIO / "output"),
    ]


def test_salida_personalizada():
    salida = SITIO.parent / "salida-alternativa"
    generar, desplegar = comandos_publicacion(salida=salida)
    assert generar[-1] == desplegar[-1] == str(salida)


@patch("ej2c5.subprocess.run")
def test_publicacion_en_orden(ejecutar):
    publicar(confirmar=True)
    assert ejecutar.call_args_list == [
        call(comando, cwd=SITIO, check=True) for comando in comandos_publicacion()
    ]


@patch("ej2c5.subprocess.run")
def test_sin_autorizacion_no_ejecuta(ejecutar):
    with pytest.raises(ValueError):
        publicar()
    ejecutar.assert_not_called()


@patch("ej2c5.subprocess.run")
def test_fallo_de_generacion_impide_despliegue(ejecutar):
    ejecutar.side_effect = subprocess.CalledProcessError(1, "pelican")
    with pytest.raises(subprocess.CalledProcessError):
        publicar(confirmar=True)
    ejecutar.assert_called_once_with(comandos_publicacion()[0], cwd=SITIO, check=True)


@patch("ej2c5.subprocess.run")
def test_fallo_de_despliegue_se_propaga(ejecutar):
    ejecutar.side_effect = [None, subprocess.CalledProcessError(1, "ghp-import")]
    with pytest.raises(subprocess.CalledProcessError):
        publicar(confirmar=True)
    assert ejecutar.call_count == 2


@patch("subprocess.run")
def test_cli_sin_flag_solo_muestra_comandos(ejecutar, monkeypatch, capsys):
    archivo = Path(__file__).resolve().parent / "ej2c5.py"
    monkeypatch.setattr("sys.argv", [str(archivo)])
    runpy.run_path(str(archivo), run_name="__main__")
    ejecutar.assert_not_called()
    assert "ghp-import -n -p -b gh-pages" in capsys.readouterr().out


@patch("subprocess.run")
def test_cli_publicar_explicito(ejecutar, monkeypatch):
    archivo = Path(__file__).resolve().parent / "ej2c5.py"
    monkeypatch.setattr("sys.argv", [str(archivo), "--publicar"])
    runpy.run_path(str(archivo), run_name="__main__")
    assert ejecutar.call_args_list == [
        call(comando, cwd=SITIO, check=True) for comando in comandos_publicacion()
    ]
