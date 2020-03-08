from flask import Blueprint, jsonify, request, render_template
import json
from service.service_area import listar as service_listar \
    , localizar as service_localizar

area_app = Blueprint('area_api', __name__, template_folder='templates')

@area_app.route('/areas', methods=['GET'])
def listar():
    areas_list = service_listar()
    return jsonify([area.__dict__() for area in areas_list])