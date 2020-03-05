from flask import Flask, request, render_template
from contextlib import closing
import sqlite3

############################
#### Definições da API. ####
############################

app = Flask(__name__)

@app.route("/")
def menu():
    return render_template("menu.html", mensagem = "")

@app.route("/cliente")
def listar_clientes_api():
    return render_template("lista_clientes.html", clientes = listar_clientes())

@app.route("/cliente/novo", methods = ["GET"])
def form_criar_cliente_api():
    return render_template("form_cliente.html", id_cliente = "novo", nome = "", sexo = "")

@app.route("/cliente/novo", methods = ["POST"])
def criar_cliente_api():
    nome = request.form["nome"]
    sexo = request.form["sexo"]
    id_cliente = criar_cliente(nome, sexo)
    return render_template("menu.html", mensagem = f"{'O' if sexo == 'M' else 'A'} cliente {nome} foi criad{'o' if sexo == 'M' else 'a'} com o id {id_cliente}.")

@app.route("/cliente/<int:id_cliente>", methods = ["GET"])
def form_alterar_cliente_api(id_cliente):
    cliente = consultar_cliente(id_cliente)
    if cliente == None:
        return render_template("menu.html", mensagem = f"Esse cliente não existe."), 404
    return render_template("form_cliente.html", id_cliente = id_cliente, nome = cliente['nome'], sexo = cliente['sexo'])

@app.route("/cliente/<int:id_cliente>", methods = ["POST"])
def alterar_cliente_api(id_cliente):
    nome = request.form["nome"]
    sexo = request.form["sexo"]
    cliente = consultar_cliente(id_cliente)
    if cliente == None:
        return render_template("menu.html", mensagem = f"Esse cliente nem mesmo existia mais."), 404
    editar_cliente(id_cliente, nome, sexo)
    return render_template("menu.html", mensagem = f"{'O' if sexo == 'M' else 'A'} cliente {nome} com o id {id_cliente} foi editad{'o' if sexo == 'M' else 'a'}.")

@app.route("/produto")
def listar_produtos_api():
    return render_template("lista_produtos.html", produtos = listar_produtos())

@app.route("/produto/novo", methods = ["GET"])
def form_criar_produto_api():
    return render_template("form_produto.html", id_produto = "novo", descricao = "", id_cliente = "", clientes = listar_clientes_ordem())

@app.route("/produto/novo", methods = ["POST"])
def criar_produto_api():
    descricao = request.form["descricao"]
    id_cliente = request.form["id_cliente"]
    id_produto = criar_produto(descricao, id_cliente)
    return render_template("menu.html", mensagem = f"O produto {descricao} foi criado com o id {id_produto}.")

@app.route("/produto/<int:id_produto>", methods = ["GET"])
def form_alterar_produto_api(id_produto):
    produto = consultar_produto(id_produto)
    if produto == None:
        return render_template("menu.html", mensagem = f"Esse produto não existe."), 404
    return render_template("form_produto.html", id_produto = id_produto, descricao = produto['descricao'], id_cliente = produto['id_cliente'], clientes = listar_clientes_ordem())

@app.route("/produto/<int:id_produto>", methods = ["POST"])
def alterar_produto_api(id_produto):
    descricao = request.form["descricao"]
    id_cliente = request.form["id_cliente"]
    produto = consultar_produto(id_produto)
    if produto == None:
        return render_template("menu.html", mensagem = f"Esse produto nem mesmo existia mais."), 404
    editar_produto(id_produto, descricao, id_cliente)
    return render_template("menu.html", mensagem = f"O produto {descricao} com o id {id_produto} foi editado.")

@app.route("/produto/<int:id_produto>", methods = ["DELETE"])
def deletar_produto_api(id_produto):
    produto = consultar_produto(id_produto)
    if produto == None:
        return render_template("menu.html", mensagem = "Esse produto nem mesmo existia mais."), 404
    deletar_produto(id_produto)
    return render_template("menu.html", mensagem = f"O produto {produto['descricao']} com o id {id_produto} foi excluído.")

###############################################
#### Funções auxiliares de banco de dados. ####
###############################################

# Converte uma linha em um dicionário.
def row_to_dict(description, row):
    if row == None:
        return None
    d = {}
    for i in range(0, len(row)):
        d[description[i][0]] = row[i]
    return d

# Converte uma lista de linhas em um lista de dicionários.
def rows_to_dict(description, rows):
    result = []
    for row in rows:
        result.append(row_to_dict(description, row))
    return result

####################################
#### Definições básicas de DAO. ####
####################################

sql_create = """
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL,
    sexo VARCHAR(1) NOT NULL
);

CREATE TABLE IF NOT EXISTS produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao VARCHAR(50) NOT NULL,
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
);
"""

def conectar():
    return sqlite3.connect('clientes.db')

def criar_bd():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.executescript(sql_create)
        con.commit()

def listar_clientes():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_cliente, nome, sexo FROM cliente ORDER BY id_cliente")
        return rows_to_dict(cur.description, cur.fetchall())

def listar_clientes_ordem():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_cliente, nome, sexo FROM cliente ORDER BY nome")
        return rows_to_dict(cur.description, cur.fetchall())

def consultar_cliente(id_cliente):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT id_cliente, nome, sexo FROM cliente WHERE id_cliente = ?", (id_cliente, ))
        return row_to_dict(cur.description, cur.fetchone())

def consultar_produto(id_produto):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT p.id_produto, p.descricao, p.id_cliente, c.nome, c.sexo FROM produto p INNER JOIN cliente c ON p.id_cliente = c.id_cliente WHERE id_produto = ?", (id_produto, ))
        return row_to_dict(cur.description, cur.fetchone())

def listar_produtos():
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("SELECT p.id_produto, p.descricao, p.id_cliente, c.nome, c.sexo FROM produto p INNER JOIN cliente c ON p.id_cliente = c.id_cliente ORDER BY p.id_produto")
        return rows_to_dict(cur.description, cur.fetchall())

def criar_cliente(nome, sexo):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO cliente (nome, sexo) VALUES (?, ?)", (nome, sexo))
        id_cliente = cur.lastrowid
        con.commit()
        return id_cliente

def criar_produto(descricao, id_cliente):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("INSERT INTO produto (descricao, id_cliente) VALUES (?, ?)", (descricao, id_cliente))
        id_produto = cur.lastrowid
        con.commit()
        return id_produto

def editar_cliente(id_cliente, nome, sexo):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE cliente SET nome = ?, sexo = ? WHERE id_cliente = ?", (nome, sexo, id_cliente))
        con.commit()

def editar_produto(id_produto, descricao, id_cliente):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("UPDATE produto SET descricao = ?, id_cliente = ? WHERE id_produto = ?", (descricao, id_cliente, id_produto))
        con.commit()

def deletar_produto(id_produto):
    with closing(conectar()) as con, closing(con.cursor()) as cur:
        cur.execute("DELETE FROM produto WHERE id_produto = ?", (id_produto, ))
        con.commit()

########################
#### Inicialização. ####
########################

if __name__ == "__main__":
    criar_bd()
    app.run()