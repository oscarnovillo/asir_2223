from flask import Blueprint, render_template, request

from app import db
from app.data.equipo_dao import EquipoDao


rutas_usuarios = Blueprint("routes", __name__)


@rutas_usuarios.route('/')
def index():
    return render_template('index.html')

@rutas_usuarios.route('/test')
def pepe():
    equipo_dao = EquipoDao()

    equipos = equipo_dao.select_all(db)

    return render_template('test.html',equipos=equipos)