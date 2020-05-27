from models.model_area import Area
from infra.dao.dao_area import listar, localizar, alterar, novo

##Service que busca todos os materiais
def listar_areas():
    return listar()

##Service que busca os materiais
def localizar_areas(filtros):
    id = filtros['id']
    status = filtros['status']
    return localizar(id, status)

##Service que cria a lista e envia para atualização
def atualiza_areas(dicionario):
    lista = []
    for item in dicionario:
        lista.append(item["id"])
    return alterar(lista)

##Service que registra uma nova area
def nova_area(area_data):
    return novo(area_data)
