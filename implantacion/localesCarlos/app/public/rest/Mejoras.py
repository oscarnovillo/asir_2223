import json

from flask import request, current_app, session, jsonify
from flask_restful import Resource

from app.public.errorHandler.CustomException import CustomException
from app.public.filters.FilterLogin import filterLogin
from app.servicios.MejorasServicios import MejorasServicios
from app.utils.Constantes import Constantes


class MejorasVoto(Resource):
    method_decorators = [filterLogin]
    mejorasServicios = MejorasServicios()

    def post(self):
        return self.mejorasServicios.addVoto(request.get_json(), session[Constantes.SESSION_ID_USER])


class Mejoras(Resource):
    method_decorators = [filterLogin]

    mejorasServicios = MejorasServicios()

    def get(self):
        if "estado" in request.values:
            return jsonify(self.mejorasServicios.obtenerMejoras(session[Constantes.SESSION_ID_LOCAL]
                                                                , session[Constantes.SESSION_ID_USER],
                                                                request.values["estado"]))
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

    def post(self):
        if 'image' in request.files:
            file = request.files['image']
            jsonStr = request.values['mejora']
            if file.filename:
                images_dir = current_app.config['PATH_IMG_PROFILE']
                url_path = current_app.config['URL_IMG_PROFILE']

                self.mejorasServicios.addMejora(images_dir, url_path, file, json.loads(jsonStr))
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        return True

    def delete(self):
        if "id" in request.values:
            self.mejorasServicios.deleteMejora(request.values["id"])
        else:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        return True
