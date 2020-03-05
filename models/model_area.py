class Area:
    def __init__(self, id, id_status=0, dt_adicao=0, dt_atualizacao=0):
        self.id = id
        self.id_status = id_status
        self.dt_adicao = dt_adicao
        self.dt_atualizacao = dt_atualizacao
    
    ##Método que cria dicionário com informação de área
    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['id_status'] = self.id_status
        d['dt_adicao'] = self.dt_adicao
        d['dt_atualizacao'] = self.dt_atualizacao

    ##Método que cria a tupla que será inserida no banco de dados
    @staticmethod
    def cria(dados):
        try:
            if "id" in dados:
                id = dados['id'] 
                id_status = dados['id_status']
                dt_adicao = dados['dt_adicao']
                dt_atualizacao = dados['dt_atualizacao']
                return Area(id=id, id_status=id_status, dt_adicao=dt_adicao,dt_atualizacao=dt_atualizacao)
        except Exception as e:
            print('Erro ao criar Area')
            print(e)
    
    ##Método utilizado para criar tuplas com dados do usuário
    @staticmethod
    def cria_tupla(registro):
        try:
                id = registro[0] 
                id_status = registro[1]
                dt_adicao = registro[2]
                dt_atualizacao = registro[3]
            return Area(id=id, id_status=id_status, dt_adicao=dt_adicao,dt_atualizacao=dt_atualizacao)
        except Exception as e:
                print('Erro ao criar Area')
                print(e)