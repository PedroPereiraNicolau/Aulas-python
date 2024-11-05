import pytest
from calculoimposto import calcular_imposto

def test_calculoimposto():
    #Teste com valores normais
    assert calcular_imposto(1000,0.1) == 100
    assert calcular_imposto(2000,0.15) == 300
def test_salario_negativo():
    with pytest.raises(ValueError):
        calcular_imposto(-1000, 0.1)
def test_aliquota_invalida():
    with pytest.raises(ValueError):
        calcular_imposto(1000, -0.1)
    with pytest.raises(ValueError):
        calcular_imposto(1000, 1.5)
def test_aliquota_zero():
    assert calcular_imposto(1000, 0) == 0    