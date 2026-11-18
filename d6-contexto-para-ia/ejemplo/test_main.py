from src.main import saludar


def test_saludar():
    assert saludar("mundo") == "Hola, mundo"
