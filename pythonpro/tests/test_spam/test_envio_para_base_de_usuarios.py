from unittest.mock import Mock

import pytest

from pythonpro.spam.main import EnviadorDeSpam
from pythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Alfonso0', email='alfareiza@gmail.com'),
            Usuario(nome='Alfredito', email='alfareiza@gmail.com')
        ],
        [
            Usuario(nome='Alfonso0', email='alfareiza@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('alfareiza@gmail.com',
                                   'Mensaje de Prueba',
                                   'Este es un mensaje de prueba')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Alfonso0', email='alfareiza@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('jcastrovq@gmail.com',
                                   'Mensaje de Prueba',
                                   'Este es un mensaje de prueba')
    enviador.enviar.assert_called_once_with('jcastrovq@gmail.com',
                                            'alfareiza@gmail.com',
                                            'Mensaje de Prueba',
                                            'Este es un mensaje de prueba')
