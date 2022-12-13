import json

from flask import jsonify, current_app, request, session
from flask_restful import Resource

from app.public.errorHandler.CustomException import CustomException
from app.public.filters.FilterLogin import filterLogin
from app.servicios.EventosServicios import EventosServicios
from app.utils.Constantes import Constantes


class Eventos(Resource):
    method_decorators = [filterLogin]

    eventosServicios = EventosServicios()

    def get(self):
        eventos = self.eventosServicios.obtenerEventosPorLocal(session[Constantes.SESSION_ID_LOCAL])
        return jsonify(eventos)

    def post(self):
        if 'image' in request.files:
            file = request.files['image']
            jsonStr = request.values['event']
            if file.filename:
                images_dir = current_app.config['PATH_IMG_PROFILE']
                url_path = current_app.config['URL_IMG_PROFILE']
                self.eventosServicios.addEvento(images_dir, url_path, file, json.loads(jsonStr))
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)
        return True

    def delete(self):
        if "id" in request.values:
            self.eventosServicios.deleteEvento(request.values["id"])
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        return True
