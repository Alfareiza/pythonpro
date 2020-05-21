from pythonpro.spam.enviador_emails import Enviador
from pythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails('alfareiza@gmail.com',
                                   'Mensaje de Prueba',
                                   'Este es un mensaje de prueba')
