class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remitente, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                remitente,
                usuario.email,
                assunto,
                corpo
            )
