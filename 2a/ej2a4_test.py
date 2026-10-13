"""Tests para upper, default y length."""

import pytest

from ej2a4 import resumir_usuario


def test_filtros():
    assert resumir_usuario({"nombre": "Ana", "cursos": ["Python", "HTML"]}) == (
        "ANA: 2 cursos"
    )


@pytest.mark.parametrize("usuario", [{}, {"nombre": ""}, {"nombre": None}])
def test_valor_por_defecto(usuario):
    assert resumir_usuario(usuario) == "INVITADO: 0 cursos"


def test_escape():
    assert resumir_usuario({"nombre": "<b>"}) == "&lt;B&gt;: 0 cursos"
