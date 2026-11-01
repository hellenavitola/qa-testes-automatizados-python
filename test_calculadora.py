import pytest

def test_soma():
    resultado = 2 + 3
    assert resultado == 5


def test_subtracao():
    resultado = 10 - 4
    assert resultado == 6


def test_multiplicacao():
    resultado = 3 * 4
    assert resultado == 12


def test_divisao():
    resultado = 10 / 2
    assert resultado == 5

import pytest


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        resultado = 10 / 0    


@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (10, 5, 15),
    (-2, 2, 0),
    (0, 0, 0),
    (100, 50, 150)
])
def test_soma_parametrizada(a, b, esperado):
    resultado = a + b
    assert resultado == esperado