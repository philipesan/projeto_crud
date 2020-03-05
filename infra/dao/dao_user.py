import sqlite3
from models.model_user import Usuario

##Método para realizar login no sistema
def logar(usuario, senha):
    con = sqlite3.connect('database.db')
    cur = con.cursor()   
    sql = (f'''
            SELECT 
                *
            FROM tb_usuarios
            WHERE 
                usuario = '{usuario}'
                AND senha = '{senha}'
            ''')
    cur.execute(sql)
    usuario_login = cur.fetchone()
    con.close()
    return usuario_login