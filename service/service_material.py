from models.model_material import Material
from infra.dao.dao_material import novo

##Service que registra uma novo material
def novo_material(material_data):
    #material_novo = Material.cria(material_data)
    #novo_material(material_novo.__dict__())
    return novo(material_data)
