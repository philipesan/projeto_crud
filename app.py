from flask import Flask, jsonify, request, render_template
from infra.database import CreateDatabase
from login_api import login_app
import sqlite3
import os

app = Flask(__name__)
app.register_blueprint(login_app)


if __name__ == '__main__':
    CreateDatabase()
    app.run(host='localhost', port=5000, debug=True)
