from flask import Blueprint, jsonify, request, render_template
import json
from service.service_area import listar_areas as service_listar \
    , localizar_areas as service_localizar \
    , atualiza_areas as service_atualiza   \
    , nova_area as service_novo

area_app = Blueprint('area_api', __name__, template_folder='templates')

@area_app.route('/areas_listar', methods=['GET'])
def listar():
    areas_list = service_listar()
    area_dict = [area.__dict__() for area in areas_list]
    if isinstance(area_dict, Exception):
        return "Erro", 503
    else:            
        return jsonify(area_dict)

@area_app.route('/areas_localizar/<string:id>/<int:status>', methods=['GET'])
def localizar(id = None, status = None):
    filtros = {"id":id, "status":status}
    areas_list = service_localizar(filtros)
    area_dict = [area.__dict__() for area in areas_list]
    if isinstance(area_dict, Exception):
        return "Erro", 503
    else:    
        return jsonify(area_dict)

@area_app.route('/areas_localizar_id/<string:id>/', methods=['GET'])
def localizar_id(id):
    filtros = {"id":id, "status":None}
    areas_list = service_localizar(filtros)
    area_dict = [area.__dict__() for area in areas_list]
    if isinstance(area_dict, Exception):
        return "Erro", 503
    else:    
        return jsonify(area_dict)

@area_app.route('/areas_localizar_status/<int:status>/', methods=['GET'])
def localizar_status(status):
    filtros = {"id":None, "status":status}
    areas_list = service_localizar(filtros)
    area_dict = [area.__dict__() for area in areas_list]
    if isinstance(area_dict, Exception):
        return "Erro", 503
    else:    
        return jsonify(area_dict)

@area_app.route('/areas', methods=['GET'])
def areas():
    return render_template("lista_areas.html")

@area_app.route('/cadastrar_areas', methods=['GET'])
def cadastrar_areas():
    return render_template("cadastra_area.html")

@area_app.route('/inativa_areas', methods=['PUT'])
def atualiza():
    alteracoes = request.get_json()
    areas_list = service_atualiza(alteracoes)
    area_dict = [area.__dict__() for area in areas_list]
    if isinstance(area_dict, Exception):
        return "Erro", 503
    else:    
        return jsonify(area_dict)

@area_app.route('/nova_area', methods=['POST'])
def nova_area():
    nova_area = request.get_json()
    ms_list = service_novo(nova_area['id'])
    if isinstance(ms_list, Exception):
        return "Erro", 503
    else:    
        return "Sucesso", 201