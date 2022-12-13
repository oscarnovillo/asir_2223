from flask import (Blueprint, current_app, jsonify, request,
                   send_from_directory, session)
from flask_api import status
from flask_mail import Message

from app.public.errorHandler.CustomException import CustomException
from app.public.filters.FilterLogin import filterLogin
from app.servicios.UsuariosServicios import UsuariosServicios
from app.utils.Constantes import Constantes

login_api = Blueprint('login_api', __name__)


@login_api.route('/login', methods=["GET", "POST"])
def login():
    usuarioServicios = UsuariosServicios()

    usuario = usuarioServicios.login(request.get_json())

    session[Constantes.SESSION_ID_LOCAL] = usuario["id_local"]
    session[Constantes.SESSION_LOGIN] = "ok"
    session[Constantes.SESSION_ID_USER] = usuario["id_usuario"]

    return jsonify(usuario)


@login_api.route('/recovery', methods=["GET", "POST"])
def recovery():
    usuarioServicios = UsuariosServicios()
    if "recovery" not in request.values or len(request.values["recovery"]) <= 0:
        raise CustomException(Constantes.COMPLETAR_CAMPOS, status.HTTP_409_CONFLICT)

    return jsonify(usuarioServicios.recoveryPassword(request.values["recovery"]))


@login_api.route('/api/usuarios/closeSession', methods=["POST"])
@filterLogin
def closeSession():
    session.clear()
    return "ok"


@login_api.route('/api/usuarios/profileImg', methods=["POST"])
@filterLogin
def addProfileImagenUsuario():
    if 'image' in request.files:
        file = request.files['image']

        if file.filename:
            images_dir = current_app.config['PATH_IMG_PROFILE']
            url_path = current_app.config['URL_IMG_PROFILE']
            usuarioServicios = UsuariosServicios()
            filePath = usuarioServicios.addPhotoUsuario(images_dir, url_path, file, session[Constantes.SESSION_ID_USER])

    return jsonify(filePath)


@login_api.route('/')
def get_exams():
    msg = Message("probando",
                  sender="app.local.tfc@gmail.com",
                  recipients=["oscar.novillo@gmail.com"])
    from app import mail
    mail.send(msg)
    return "hello world 2"


@login_api.route('/images/<filename>')
def media_posts(filename):
    dir_path = current_app.config['PATH_IMG_PROFILE']
    return send_from_directory(dir_path, filename)
