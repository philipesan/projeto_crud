from flask import Flask, jsonify, request, render_template
from login_api import login_app
from area_api import area_app
import sqlite3
import os

app = Flask(__name__)
app.register_blueprint(login_app)
app.register_blueprint(area_app)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
