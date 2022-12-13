from flask import jsonify, request
from flask_api import status
from flask_restful import Resource

from app.public.filters.FilterLogin import filterLogin
from app.servicios.LocalesServicios import LocalesServicios


class LocalesGet(Resource):
    method_decorators = {'get': [filterLogin]}

    def get(self, idLocal):
        localesServicios = LocalesServicios()

        return jsonify(localesServicios.getLocal(idLocal))


class Locales(Resource):
    method_decorators = {'get': [filterLogin], 'put': [filterLogin]}
    localesServicios = LocalesServicios()

    def post(self):
        usuarioAdminLocal = self.localesServicios.addLocal(request.get_json())
        response = jsonify(usuarioAdminLocal)
        response.status_code = status.HTTP_201_CREATED
        return response

    def put(self):
        return jsonify(self.localesServicios.updateLocal(request.get_json()))
