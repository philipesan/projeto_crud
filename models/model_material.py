class Material:
    def __init__(self, id, descricao, custo, vendedor, fabricante, unidade_medida, grupo, alimentacao, capacidade, resistencia, id_status=0, dt_adicao=0, dt_atualizacao=0):
        self.id = id
        self.descricao = descricao
        self.custo = custo
        self.vendedor = vendedor
        self.fabricante = fabricante
        self.unidade_medida = unidade_medida
        self.grupo = grupo
        self.alimentacao = alimentacao
        self.capacidade = capacidade
        self.resistencia = resistencia
        self.id_status = id_status
        self.dt_adicao = dt_adicao
        self.dt_atualizacao = dt_atualizacao
    
    ##Método que cria dicionário com informação de Material
    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['descricao'] = self.descricao
        d['custo'] = self.custo
        d['vendedor'] = self.vendedor
        d['fabricante'] = self.fabricante
        d['unidade_medida'] = self.unidade_medida
        d['grupo'] = self.grupo
        d['alimentacao'] = self.alimentacao
        d['capacidade'] = self.capacidade
        d['resistencia'] = self.resistencia    
        d['id_status'] = self.id_status
        d['dt_adicao'] = self.dt_adicao
        d['dt_atualizacao'] = self.dt_atualizacao
        return d

    ##Método que cria a tupla que será inserida no banco de dados
    @staticmethod
    def cria(dados):
        try:
            if "id" in dados:
                id = dados['id']
                descricao = dados['descricao']
                custo = dados['custo']
                vendedor = dados['vendedor']
                fabricante = dados['fabricante']
                unidade_medida = dados['unidade_medida']
                grupo = dados['grupo']
                alimentacao = dados['alimentacao'] 
                capacidade = dados['capacidade'] 
                resistencia = dados['resistencia'] 
                id_status = dados['id_status']
                dt_adicao = dados['dt_adicao']
                dt_atualizacao = dados['dt_atualizacao'] 
                return Material(id=id, descricao=descricao, custo=custo, vendedor=vendedor,\
                 fabricante=fabricante, unidade_medida=unidade_medida, grupo=grupo,\
                 alimentacao=alimentacao, capacidade=capacidade, resistencia=resistencia,\
                 id_status=id_status, dt_adicao=dt_adicao, dt_atualizacao=dt_atualizacao)
        except Exception as e:
            print('Erro ao criar Material')
            print(e)

    ##Método utilizado para criar tuplas com dados do usuário
    @staticmethod
    def cria_tupla(registro):
        try:
            id = registro[0]
            descricao = registro[1]
            custo = registro[2]
            vendedor = registro[3]
            fabricante = registro[4]
            unidade_medida = registro[5]
            grupo = registro[6]
            alimentacao = registro[7] 
            capacidade = registro[8] 
            resistencia = registro[9] 
            id_status = registro[10]
            dt_adicao = registro[11]
            dt_atualizacao = registro[12] 
            return Material(id=id, descricao=descricao, custo=custo, vendedor=vendedor,\
                 fabricante=fabricante, unidade_medida=unidade_medida, grupo=grupo,\
                 alimentacao=alimentacao, capacidade=capacidade, resistencia=resistencia,\
                 id_status=id_status, dt_adicao=dt_adicao, dt_atualizacao=dt_atualizacao)
        except Exception as e:
                print('Erro ao criar Material')
                print(e)