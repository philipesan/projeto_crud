from models.model_user import Usuario
from infra.dao.dao_user import logar

def fazer_login(usuario_login):
    try:
        usuario = usuario_login['usuario']
        senha = usuario_login['senha']
        credenciais = logar(usuario, senha)
        if (credenciais):
            return True
        else:
            return False
    except Exception as e:
        print('Erro ao Fazer Login')
        print(e)


usuario_login = [{"usuario":"teste", "senha":"teste"}]
fazer_login(usuario_login)