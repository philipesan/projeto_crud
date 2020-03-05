import sqlite3
from models.model_area import Area

##Método que busca áreas no banco de dados
def listar(area, status = None, dt_adicao = None, dt_alteracao = None):
    areas = []
    con = sqlite3.connect('database.db')
    cur = con.cursor()   
    sql = (f'''
            SELECT 
                *
            FROM tb_usuarios
            WHERE 
                id = '{area}'
            ''')
    if (status):
        sql = sql + (f"\n AND status = '{status}'")
    if (dt_adicao):
        sql = sql + (f"\n AND dt_adicao = '{dt_adicao}'")
    if (dt_alteracao):
        sql = sql + (f"\n AND dt_adicao = '{dt_alteracao}'")

    cur.execute(sql)

    areas = [Area.cria_tupla(linha) \
        for linha in cur.fetchall()]

    con.close()
    return areas
