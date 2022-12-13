from flask import jsonify, request, session
from flask_api import status
from flask_restful import Resource

from app.public.filters.FilterLogin import filterLogin
from app.servicios.UsuariosServicios import UsuariosServicios
from app.utils.Constantes import Constantes


class Usuarios(Resource):
    method_decorators = {'get': [filterLogin], 'put': [filterLogin]}

    def get(self):
        usuariosServicios = UsuariosServicios()
        return jsonify(usuariosServicios.getUsuariosByIdLocal(session[Constantes.SESSION_ID_LOCAL]))

    def post(self):
        usuariosServicios = UsuariosServicios()
        usuario = usuariosServicios.addUsuario(request.get_json())
        response = jsonify(usuario)
        response.status_code = status.HTTP_201_CREATED
        return response

    def put(self):
        usuariosServicios = UsuariosServicios()
        usuariosServicios.updateUsuario(request.get_json(), session[Constantes.SESSION_ID_USER])
        return jsonify("True")
