from flask import Blueprint, jsonify, request, render_template
import json
from service.service_material import novo_material as service_novo

material_app = Blueprint('material_api', __name__, template_folder='templates')

@material_app.route('/cadastrar_materiais', methods=['GET'])
def cadastrar_areas():
    return render_template("cadastra_material.html")

@material_app.route('/novo_material', methods=['POST'])
def novo_material():
    novo_material = request.get_json()
    print(novo_material)
    ms_list = service_novo(novo_material)
    if isinstance(ms_list, Exception):
        return "Erro", 503
    else:    
        return "Sucesso", 201
