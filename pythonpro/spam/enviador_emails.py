class Enviador():
    def enviar(self, remitente, destinatario, assunto, corpo):
        if '@' not in remitente:
            raise (EmailInvalido(f'Email inválido: {remitente}'))
        return remitente


class EmailInvalido(Exception):
    pass
