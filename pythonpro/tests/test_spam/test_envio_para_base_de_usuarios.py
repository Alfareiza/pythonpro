import pytest

from pythonpro.spam.enviador_emails import Enviador
from pythonpro.spam.main import EnviadorDeSpam
from pythonpro.spam.modelos import Usuario

class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remitente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remitente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1

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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('alfareiza@gmail.com',
                                   'Mensaje de Prueba',
                                   'Este es un mensaje de prueba')
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Alfonso0', email='alfareiza@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('jcastrovq@gmail.com',
                                   'Mensaje de Prueba',
                                   'Este es un mensaje de prueba')
    assert enviador.parametros_de_envio == ('jcastrovq@gmail.com',
                                            'alfareiza@gmail.com',
                                            'Mensaje de Prueba',
                                            'Este es un mensaje de prueba')

