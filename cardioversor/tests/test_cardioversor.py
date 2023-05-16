import pytest
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
from cardioversor import *

@pytest.fixture
def cardioversor():
    return Cardioversor()

def test_inicializacao(cardioversor):
    assert cardioversor.freq_cardiaca == 0
    assert not cardioversor.identificador_marca_passo
    assert cardioversor.potencia == 10
    assert cardioversor.frequencia == 0
    assert not cardioversor.ligado

def test_set_identificador_marca_passo(cardioversor):
    cardioversor.set_identificador_marca_passo(True)
    assert cardioversor.identificador_marca_passo

def test_set_potencia(cardioversor):
    potencia = 15
    cardioversor.set_potencia(potencia)
    assert cardioversor.potencia == potencia

def test_set_frequencia(cardioversor):
    frequencia = 50
    cardioversor.set_frequencia(frequencia)
    assert cardioversor.frequencia == frequencia

def test_ligar(cardioversor):
    resultado = cardioversor.ligar()
    assert resultado == {"message": "Cardioversor ligado com sucesso"}
    assert cardioversor.ligado

    resultado = cardioversor.desligar()
    cardioversor.set_identificador_marca_passo(True)
    resultado = cardioversor.ligar()
    assert resultado == {"aviso": "Marca passo identificado"}
    assert not cardioversor.ligado

def test_desligar(cardioversor):
    cardioversor.ligar()  # Ligar o cardioversor antes de desligar
    cardioversor.desligar()
    assert not cardioversor.ligado

def test_get_status(cardioversor):
    resultado = cardioversor.get_status()
    assert resultado == {
        "cardioversor": {
            "freq_cardiaca": cardioversor.freq_cardiaca,
            "identificador_marca_passo": cardioversor.identificador_marca_passo,
            "potencia": cardioversor.potencia,
            "frequencia": cardioversor.frequencia,
            "ligado": cardioversor.ligado
        }
    }