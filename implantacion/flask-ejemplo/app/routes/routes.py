from flask import Blueprint, render_template, request

from app.servicios.userServicios import UserServicios
from app import db


bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        param = request.form['q']
        return render_template('post.html',parametro = param)
    else:
        return render_template('index.html')
    

@bp.route('/verTodos')
def ver_todos():
    user_services = UserServicios(db)
    return render_template('listado.html',usuarios = user_services.get_all())

