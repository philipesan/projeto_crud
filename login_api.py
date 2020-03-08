from flask import Blueprint, jsonify, request, render_template, redirect, url_for
import json
from service.service_user import fazer_login

login_app = Blueprint('login_api', __name__, template_folder='templates')

@login_app.route("/")
def login():
    return render_template("tela_login.html")

@login_app.route("/login", methods=['POST'])
def credenciais():
    usuario_login = request.get_json()
    status_login = fazer_login(usuario_login)
    if status_login:
        return redirect(url_for('login_api.menu'))
    else:
        return 'Senha ou usuário incorretos', 403

@login_app.route("/menu")
def menu():
    return render_template("menu.html")