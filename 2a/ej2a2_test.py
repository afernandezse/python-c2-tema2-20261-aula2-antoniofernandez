"""Tests para if/elif/else."""

import pytest

from ej2a2 import clasificar_nota


@pytest.mark.parametrize(
    "nota,resultado",
    [(0, "Suspenso"), (4.9, "Suspenso"), (5, "Aprobado"),
     (8.9, "Aprobado"), (9, "Excelente"), (10, "Excelente")],
)
def test_condicionales(nota, resultado):
    assert clasificar_nota(nota) == resultado
