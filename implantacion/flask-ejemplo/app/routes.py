from flask import Blueprint, render_template, request

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Procesar formulario de inicio de sesión
        pass
    else:
        return render_template('login.html')
