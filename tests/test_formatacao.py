from text_utils import inverter_texto, contar_palavras


def test_inverter_texto():
    assert inverter_texto("abc") == "cba"


def test_contar_palavras():
    assert contar_palavras("ola mundo python") == 3
