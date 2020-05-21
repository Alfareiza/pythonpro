from pythonpro.spam.modelos import Usuario


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Alfonso0', email='alfareiza@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Alfonso1', email='alfareiza@gmail.com'),
                Usuario(nome='Alfredito', email='alfareiza@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

