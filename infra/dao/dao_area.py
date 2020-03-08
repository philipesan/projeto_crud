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
                *
            FROM tb_areas
            WHERE 1=1
            ''')
    if (area):
        sql = sql + (f"\n AND id = '{area}'")
    if (status):
        sql = sql + (f"\n AND id_status = '{status}'")

    cur.execute(sql)

    areas = cur.fetchall()

    con.close()
    return areas

##Método que localiza áreas no banco de dados
def listar():
    areas = []
    con = psycopg2.connect(user = "admin",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()   
    sql = (f'''
            SELECT 
                *
            FROM tb_areas
            WHERE id_status = 0
            ''')

    cur.execute(sql)
    areas = cur.fetchall()
    for row in areas:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))

    areas = [Area.cria_tupla(linha) \
        for linha in cur.fetchall()]

    con.close()
    return areas