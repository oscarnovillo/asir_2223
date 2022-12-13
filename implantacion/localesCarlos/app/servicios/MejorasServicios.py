import os

from marshmallow import ValidationError
from werkzeug.utils import secure_filename

from app.dao.MejorasDao import MejorasDao
from app.dao.dto.MejoraDto import MejoraDto
from app.dao.modelo.Votacion import Votacion
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes


class MejorasServicios:
    mejorasDao = MejorasDao()

    def obtenerMejoras(self, idLocal, idUserLogin, estado):
        mejorasDB = self.mejorasDao.obtenerMejoras(idLocal, idUserLogin, estado)
        schema = MejoraDto(many=True)
        return schema.dump(mejorasDB)

    def addMejora(self, images_dir, url_path, file, mejoraJson):

        image_name = secure_filename(file.filename)
        os.makedirs(images_dir, exist_ok=True)
        file_path = os.path.join(images_dir, image_name)
        if os.path.exists(file_path):
            raise CustomException(description=Constantes.FICHERO_EXISTENTE)
        file.save(file_path)
        try:
            mejora = MejoraDto().load(mejoraJson)
        except ValidationError:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)
        mejora.url_img = url_path + image_name
        self.mejorasDao.addMejora(mejora)

        return True

    def addVoto(self, mejoraJson, idUserLogin):
        try:
            mejora = MejoraDto().load(mejoraJson)
            mejora.id = mejoraJson["id"]
            votacion = Votacion(id_mejora=mejoraJson["id"], id_usuario=idUserLogin, decision=mejoraJson["voto"])
        except ValidationError:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)
        if votacion.decision is None or votacion.decision == "":
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        self.mejorasDao.addVoto(mejora, votacion)

        return True

    def deleteMejora(self, idMejora):
        return self.mejorasDao.deleteEvento(idMejora)
