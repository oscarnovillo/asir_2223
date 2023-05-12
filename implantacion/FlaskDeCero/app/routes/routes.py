import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.equipo_dao import EquipoDao


rutas_coches = Blueprint("routes", __name__)


@rutas_coches.route('/')
def index():
    return render_template('index.html')

@rutas_coches.route('/nueva')
def nueva():
    loquequiera=random.randint(1,100)
    loquequiera2=random.randint(1,100)


    return render_template('nueva.html',aleatorio1=loquequiera,aleatorio2=loquequiera2)

@rutas_coches.route('/verEquipos')
def verEquipos():
    equipo_dao = EquipoDao()

    equipos = equipo_dao.select_all(db)



    return render_template('test.html',equipos=equipos)




@rutas_coches.route('/addEquipo', methods=['POST'])   
def addEquipo():
    equipo_dao = EquipoDao()

    nombre = request.form['tuputamadre']
    ciudad = request.form['ciudad']

    if (nombre == "" or ciudad == ""):
        return redirect(url_for('routes.verEquipos'))

    equipo_dao.insert(db,nombre,ciudad)
   
    return redirect(url_for('routes.verEquipos'))    

@rutas_coches.route('/delEquipo', methods=['POST'])   
def delEquipo():
    equipo_dao = EquipoDao()

    id = request.form['id']



    equipo_dao.delete(db,id)
   
    return redirect(url_for('routes.verEquipos'))    

@rutas_coches.route('/updateEquipo', methods=['POST'])   
def updateEquipo():
    equipo_dao = EquipoDao()

    id = request.form['id']
    nombre = request.form['tuputamadre']
    ciudad = request.form['ciudad']

    if (ciudad == ""):
        equipo_dao.updateNombre(db,id,nombre)
    else:
        equipo_dao.update(db,id,nombre,ciudad)
   
    return redirect(url_for('routes.verEquipos'))    
