import psycopg2
from models.model_area import Area

##Método que localiza áreas no banco de dados
def localizar(area = None, status = None):
    areas = []
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()   
    sql = (f'''
            SELECT 
                    id
                ,   id_status
                ,   TO_CHAR(dt_adicao, 'dd/mm/yyyy')                
                ,   TO_CHAR(dt_atualizacao, 'dd/mm/yyyy')
            FROM tb_areas
            WHERE 1=1
            ''')
    if (area):
        sql = sql + (f"\n AND id = '{area}'")
    if (status):
        sql = sql + (f"\n AND id_status = '{status}'")

    cur.execute(sql)
    areas = cur.fetchall()
    areas = [Area.cria_tupla(linha) \
       for linha in areas]

    con.close()
    return areas

##Método que localiza áreas no banco de dados
def listar():
    areas = []
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()   
    sql = (f'''
            SELECT 
                    id
                ,   id_status
                ,   TO_CHAR(dt_adicao, 'dd/mm/yyyy')                
                ,   TO_CHAR(dt_atualizacao, 'dd/mm/yyyy')
            FROM tb_areas
            WHERE id_status = 0
            ''')
    cur.execute(sql)
    areas = cur.fetchall()
    areas = [Area.cria_tupla(linha) \
       for linha in areas]
    con.close()
    return areas

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
            sql = (f"""
                    UPDATE tb_areas
                    SET ID_STATUS =
                        CASE ID_STATUS
                        when 1
                        then 0
                        else 1
                        end,
                        dt_atualizacao = current_date
                    where id = '{area}'
                """)
            cur.execute(sql)
            con.commit()
        except Exception as e:
            return e
    ## Retorna os itens atualizados
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
        sql = sql + f"'{area}',"
    sql = sql + " 'barrel_roll')" 
    cur.execute(sql)
    retorno = cur.fetchall()
    retorno = [Area.cria_tupla(linha) \
       for linha in retorno]

    con.close()
    return retorno
