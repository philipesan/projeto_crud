import psycopg2
from models.model_material import Material

##Método que insere no banco uma area nova
def novo(Material):
    con = psycopg2.connect(user = "postgres",
                            password = "admin",
                            host = "localhost",
                            port = "5432",
                            database = "CrudApplication") 
    cur = con.cursor()
    try:   
        sql = """
                INSERT INTO tb_materiais 
                (
                      descricao
                    , custo
                    , vendedor
                    , fabricante
                    , unidade_medida
                    , grupo
                    , alimentacao
                    , capacidade
                    , resistencia
                    , id_status
                    , dt_adicao
                    , dt_atualizacao
                )
                VALUES
                (
                      %s
                    , %s
                    , %s
                    , %s
                    , %s
                    , %s
                    , %s
                    , %s
                    , %s
                    , '0'
                    , CURRENT_DATE
                    , CURRENT_DATE
                )
                RETURNING
                (
                    id
                )
                
                """
        cur.execute(sql, (Material['descricao'], Material['custo'], Material['vendedor']\
                    , Material['fabricante'], Material['unidade_medida'], Material['grupo']\
                    , Material['alimentacao'], Material['capacidade'], Material['resistencia']))
        new_area = cur.fetchone()
        con.commit()
        con.close()
        return new_area
    except Exception as e:
        print(e)
        return e
