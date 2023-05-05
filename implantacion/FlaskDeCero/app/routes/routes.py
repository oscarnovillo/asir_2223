from flask import Blueprint, render_template, request

from app import db
from app.data.equipo_dao import EquipoDao


rutas_coches = Blueprint("routes", __name__)


@rutas_coches.route('/')
def index():
    return render_template('index.html')

@rutas_coches.route('/nueva')
def nueva():
    return render_template('nueva.html')

@rutas_coches.route('/test')
def pepe():
    equipo_dao = EquipoDao()

    equipos = equipo_dao.select_all(db)

    return render_template('test.html',equipos=equipos)