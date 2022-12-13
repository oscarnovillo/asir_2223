import os

from werkzeug.utils import secure_filename
from marshmallow import ValidationError

from app.dao.RecibosDao import RecibosDao
from app.dao.dto.ReciboDto import ReciboDto
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes


class RecibosServicios:

    recibosDAO = RecibosDao()

    def addRecibo(self, reciboJSON):

        try:
            recibo = ReciboDto().load(reciboJSON)
        except ValidationError:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        reciboDB = self.recibosDAO.addRecibo(recibo)
        schema = ReciboDto()
        return schema.dump(reciboDB)

    def getRecibosUsuario(self, id):
        recibosDB = self.recibosDAO.getRecibosUsuarios(id)
        schema = ReciboDto(many=True)
        return schema.dump(recibosDB)

    def getRecibosLocal(self, id):
        recibosDB = self.recibosDAO.getRecibosUsuarios(id)
        schema = ReciboDto(many=True)
        return schema.dump(recibosDB)

    def verificarPago(self, idLocal, idUser):
        reciboDB =self.recibosDAO.verificarPago(idLocal, idUser)
        schema = ReciboDto()
        return schema.dump(reciboDB)

    def addJustificante(self, pdf_dir, pdf_path, file, reciboJson):
        pdf_name = secure_filename(file.filename)
        os.makedirs(pdf_dir, exist_ok=True)
        file_path = os.path.join(pdf_dir, pdf_name)
        if os.path.exists(file_path):
            raise CustomException(description=Constantes.FICHERO_EXISTENTE)
        file.save(file_path)
        try:
            recibo = ReciboDto().load(reciboJson)
            recibo.id_recibo = reciboJson['id_recibo']
        except ValidationError as e:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)
        recibo.url_pdf = pdf_path + pdf_name
        return self.recibosDAO.addJustificante(recibo)

    def deleteRecibo(self, id):
        return self.recibosDAO.deleteRecibo(id)
