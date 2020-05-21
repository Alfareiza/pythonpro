import pytest

from pythonpro.spam.enviador_emails import Enviador, EmailInvalido


def test_create_enviador_emails():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
                        'remitente',
                        ['alfareiza@gmail.com', 'foo@bar.com.br'])
def test_remetente(remitente):
    enviador = Enviador()
    resultado = enviador.enviar(remitente,
                                'jcastrovq@gmail.com',
                                'Probando Test de Correos',
                                'Este es un mensaje de prueba, ok?'
                                )
    assert remitente in resultado


@pytest.mark.parametrize('remitente', ['', 'foobar.com.br'])
def test_remetente_invalido(remitente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(remitente,
                                    'jcastrovq@gmail.com',
                                    'Probando Test de Correos',
                                    'Este es un mensaje de prueba, ok?')
