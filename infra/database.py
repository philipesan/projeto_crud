import sqlite3
import os

def CreateDatabase():
    #inicializacao do bd
    exists = os.path.isfile('.\database.db')

    if exists:
        print("Banco de dados localizado")
    else:
        print("Criando banco de dados")
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        ##Criação da tabela de locais
        print("Criando tabela de areas")
        sql = '''
            CREATE TABLE IF NOT EXISTS tb_areas( 
              id             TEXT       primary key
            , id_status      INTEGER    NOT NULL
            , dt_adicao      TEXT       NOT NULL
            , dt_atualizacao TEXT       NOT NULL
            );
            '''
        cur.execute(sql)
        con.commit()
        sql = '''            
            CREATE INDEX idx_areas 
            ON tb_areas(id);
            '''
        cur.execute(sql)
        con.commit()
        print("Criando tabela de pessoas")
        ##Criação da tabela Pessoas
        sql = '''

            CREATE TABLE IF NOT EXISTS tb_pessoas( 
              id              INTEGER      primary key autoincrement
            , nome            TEXT         NOT NULL
            , cpf_cnpj        TEXT         NOT NULL
            , tipo            INTEGER      NOT NULL
            , rua             TEXT
            , bairro          TEXT
            , numero          TEXT
            , complemento     TEXT
            , telefone        TEXT
            , site            TEXT
            , email           TEXT
            , id_status       INTEGER      NOT NULL
            , dt_adicao       TEXT         NOT NULL
            , dt_atualizacao  TEXT         NOT NULL
            )
            '''    
        cur.execute(sql)
        con.commit()
        sql = '''
            CREATE INDEX idx_pessoas 
            ON tb_pessoas(id);
        '''
        print("Criando tabela de materiais")
        ##Criação da tabela materiais
        sql = '''
            CREATE TABLE IF NOT EXISTS tb_materiais( 
            id              INTEGER      PRIMARY KEY AUTOINCREMENT
            , descricao       VARCHAR(25)  NOT NULL
            , custo           REAL         NOT NULL
            , vendedor        INTEGER      NOT NULL
            , fabricante      INTEGER      NOT NULL
            , unidade_medida  TEXT         NOT NULL
            , grupo           INTEGER      NOT NULL
            , alimentacao     INTEGER
            , capacidade      INTEGER
            , resistencia     INTEGER
            , id_status       INTEGER      NOT NULL
            , dt_adicao       TEXT         NOT NULL
            , dt_atualizacao  TEXT         NOT NULL
            ,CONSTRAINT fk_material_vendedor   FOREIGN KEY(vendedor)     REFERENCES tb_pessoas(id)
            ,CONSTRAINT fk_material_fabricante FOREIGN KEY(fabricante)   REFERENCES tb_pessoas(id)
            );
            '''
        cur.execute(sql)
        con.commit()
        sql = '''            
            CREATE INDEX idx_materiais 
            ON tb_materiais(id);            
        '''
        cur.execute(sql)
        con.commit()
        print("Criando tabela de estoque")
        ##Criação da tabela estoque
        sql = '''
            CREATE TABLE IF NOT EXISTS tb_estoque( 
              area            TEXT          NOT NULL
            , item            INTEGER       NOT NULL
            , quantidade      INTEGER       NOT NULL
            , id_status       INTEGER       NOT NULL
            , dt_adicao       TEXT          NOT NULL
            , dt_atualizacao  TEXT          NOT NULL
            ,CONSTRAINT fk_estoque_area   FOREIGN KEY(area)     REFERENCES tb_areas(id)
            ,CONSTRAINT fk_estoque_item   FOREIGN KEY(item)     REFERENCES tb_items(id)
            );
        '''
        cur.execute(sql)
        con.commit()
        sql = '''
            CREATE INDEX idx_estoque 
            ON tb_estoque(area, item);
        '''
        cur.execute(sql)
        con.commit()

        print("Criando tabela de transação")
        ##Criação da tabela transação
        sql = '''
            CREATE TABLE IF NOT EXISTS tb_transacao( 
              id              INTEGER      PRIMARY KEY AUTOINCREMENT
            , item			  INTEGER       NOT NULL   
            , area    		  TEXT          NOT NULL
            , cliente 		  INTEGER       NOT NULL
            , quantidade      INTEGER       NOT NULL
            , tipo            INTEGER       NOT NULL
            , dt_adicao       TEXT          NOT NULL
            , dt_atualizacao  TEXT          NOT NULL
            ,CONSTRAINT fk_transacao_area   	FOREIGN KEY(area)     REFERENCES tb_areas(id)
			,CONSTRAINT fk_transacao_item   	FOREIGN KEY(item)     REFERENCES tb_items(id)
			,CONSTRAINT fk_transacao_cliente	FOREIGN KEY(cliente)  REFERENCES tb_pessoas(id)			
            );
            '''
        cur.execute(sql)
        con.commit()
        sql = '''
            CREATE INDEX idx_transacao 
            ON tb_transacao(id);
        '''
        cur.execute(sql)
        con.commit()
        print("Criando tabela de usuarios")
        ##Criação da tabela transação
        sql = '''
            CREATE TABLE IF NOT EXISTS tb_usuarios( 
              id              INTEGER      PRIMARY KEY AUTOINCREMENT
            , usuario       TEXT          NOT NULL
            , senha         TEXT          NOT NULL
            , email         TEXT          NOT NULL			
            );
            '''
        cur.execute(sql)
        con.commit()
        sql = '''
            INSERT INTO tb_usuarios( 
              usuario
            , senha
            , email
            )
            VALUES(
              'admin'
            , 'admin'
            , 'admin@protostock.com.br'
            )
            '''
        cur.execute(sql)
        con.commit()
        print("Criado usuário admin")
        con.close()
        print("Tabelas criadas com sucesso!")
