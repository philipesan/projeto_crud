from models.model_area import Area
from infra.dao.dao_area import listar, localizar

##Service que busca todos os materiais
def listar_areas():
    return listar()

##Service que busca os materiais
def localizar_areas(filtros):
    id = filtros['id']
    status = filtros['status']
    return localizar(id, status)

