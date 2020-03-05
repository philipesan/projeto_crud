class Usuario:
    def __init__(self, usuario, senha, id, email):
        self.usuario = usuario
        self.senha = senha
        self.id = id
        self.email = email

    ##Método que cria um dicionário com as informações do usuário
    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['usuario'] = self.usuario
        d['senha'] = self.senha
        d['email'] = self.email

    ##Método que cria a tupla que será inserida no banco de dados
    @staticmethod
    def cria(dados):
        try:
            if "id" in dados:
                id = dados['id'] 
                usuario = dados['usuario']
                senha = dados['senha']
                email = dados['email']
                return Usuario(id=id, usuario=usuario, senha=senha,email=email)
        except Exception as e:
            print('Erro ao criar usuário')
            print(e)
    
    ##Método utilizado para criar tuplas com dados do usuário
    @staticmethod
    def cria_tupla(registro):
        try:
            id	= registro[0] 
            usuario = registro[1]
            senha = registro[2]
            email = registro[3]
            return Usuario(id=id, usuario=usuario, senha=senha,email=email)
        except Exception as e:
                print('Erro ao criar usuário')
                print(e)

