import os

from marshmallow import ValidationError
from werkzeug.utils import secure_filename

from app.dao.EventosDao import EventosDao
from app.dao.dto.EventoDto import EventoDto
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes


class EventosServicios:
    eventosDao = EventosDao()

    def addEvento(self, images_dir, url_path, file, eventoJson):
        try:
            evento = EventoDto().load(eventoJson)
        except ValidationError:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        image_name = secure_filename(file.filename)
        os.makedirs(images_dir, exist_ok=True)
        file_path = os.path.join(images_dir, image_name)
        file.save(file_path)
        evento.url_img = url_path + image_name

        self.eventosDao.addEvento(evento)

        return True

    def obtenerEventosPorLocal(self, idLocal):
        eventosDb = self.eventosDao.obtenerEventosPorIdLocal(idLocal)
        schema = EventoDto(many=True)
        return schema.dump(eventosDb)

    def deleteEvento(self, idEvento):
        return self.eventosDao.deleteEvento(idEvento)
