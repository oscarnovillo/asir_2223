from flask import request, jsonify, session, current_app
from flask_restful import Resource
import json

from app.public.errorHandler.CustomException import CustomException
from app.public.filters.FilterLogin import filterLogin
from app.servicios.RecibosServicios import RecibosServicios
from app.utils.Constantes import Constantes


class Recibos(Resource):
    method_decorators = [filterLogin]
    recibosServicios = RecibosServicios()

    def get(self):
        if "id" in request.values:
            return jsonify(self.recibosServicios.getRecibosUsuario(request.values["id"]))
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

    def post(self):
        return jsonify(self.recibosServicios.addRecibo(request.get_json()))

    def delete(self):
        if "id" in request.values:
            return self.recibosServicios.deleteRecibo(request.values["id"])
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)


class RecibosGetLocal(Resource):
    method_decorators = [filterLogin]
    recibosServicios = RecibosServicios()

    def get(self):
        return jsonify(self.recibosServicios
                       .getRecibosLocal(session[Constantes.SESSION_ID_LOCAL]))


class RecibosUtils(Resource):
    method_decorators = [filterLogin]
    recibosServicios = RecibosServicios()

    def get(self):
        return jsonify(self.recibosServicios.verificarPago(session[Constantes.SESSION_ID_LOCAL],
                                                           session[Constantes.SESSION_ID_USER]))

    def post(self):
        if 'recibo' in request.files:
            file = request.files['recibo']
            jsonStr = request.values['objectRecibo']
            if file.filename:
                pdf_dir = current_app.config['PATH_PDF']
                pdf_path = current_app.config['URL_PDF']
                return self.recibosServicios.addJustificante(pdf_dir, pdf_path, file, json.loads(jsonStr))
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)
