import psycopg2
from models.model_area import Area


##Método que localiza áreas no banco de dados
def localizar(area: str = None, status: str = None):
    areas = []
    str_parametros = []
    print(type(area))
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()   
    try:
        sql = ('''
                SELECT 
                        id
                    ,   id_status
                    ,   TO_CHAR(dt_adicao, 'dd/mm/yyyy')                
                    ,   TO_CHAR(dt_atualizacao, 'dd/mm/yyyy')
                FROM tb_areas
                WHERE 1=1
                ''')
        if (area):
            sql = sql + ("\n AND id = %s")
            str_parametros.append(area)
        if (status != None):
            sql = sql + ("\n AND id_status = %s")
            str_parametros.append(status)
        sql += "ORDER BY id"
        cur.execute(sql, str_parametros)
        areas = cur.fetchall()
        areas = [Area.cria_tupla(linha) \
        for linha in areas]

        con.close()
        return areas
    except Exception as e:
        print(type(e))
        return e

##Método que localiza áreas no banco de dados
def listar():
    areas = []
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()   
    try:
        sql = (f'''
                SELECT 
                        id
                    ,   id_status
                    ,   TO_CHAR(dt_adicao, 'dd/mm/yyyy')                
                    ,   TO_CHAR(dt_atualizacao, 'dd/mm/yyyy')
                FROM tb_areas
                ORDER BY id
                ''')
        cur.execute(sql)
        areas = cur.fetchall()
        areas = [Area.cria_tupla(linha) \
        for linha in areas]
        con.close()
        return areas
    except Exception as e:
        return e

##Método que altera o status das areas no banco de dados
def alterar(areas):
    retorno = []
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()   
    for area in areas:
        try:   
            sql = ("""
                    UPDATE tb_areas
                    SET ID_STATUS =
                        CASE ID_STATUS
                        when 1
                        then 0
                        else 1
                        end,
                        dt_atualizacao = current_date
                    where id = %s
                """)
            cur.execute(sql, [area])
            con.commit()
        except Exception as e:
            return e
    ## Retorna os itens atualizados
    try:   
        sql = (f'''
                SELECT 
                        id
                    ,   id_status
                    ,   TO_CHAR(dt_adicao, 'dd/mm/yyyy')                
                    ,   TO_CHAR(dt_atualizacao, 'dd/mm/yyyy')
                FROM tb_areas
                WHERE id IN (            
            ''')
        for area in areas:
            sql = sql + "%s,"
        sql = sql + " 'barrel_roll')" 
        cur.execute(sql, areas)
        retorno = cur.fetchall()
        retorno = [Area.cria_tupla(linha) \
        for linha in retorno]
        con.close()
        return retorno
    except Exception as e:
        return e

##Método que insere no banco uma area nova
def novo(area):
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()
    try:   
        sql = f"""
                INSERT INTO tb_areas 
                (
                    id
                    , id_status
                    , dt_adicao
                    , dt_atualizacao
                )
                VALUES
                (
                  '{area}'
                , '0'
                , CURRENT_DATE
                , CURRENT_DATE 
                )
                RETURNING
                (
                    id
                )
                
                """
        cur.execute(sql)
        new_area = cur.fetchone()
        con.commit()
        con.close()
        return new_area
    except Exception as e:
        return e
