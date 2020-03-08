import psycopg2
from models.model_user import Usuario

##Método para realizar login no sistema
def logar(usuario, senha):
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
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