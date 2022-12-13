from marshmallow import ValidationError

from app.dao.LocalesDao import LocalesDao
from app.dao.dto.LocalDto import LocalDto
from app.dao.dto.UsuarioAdminLocal import UsuarioAdminLocal
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes
from app.utils.PasswordHash import get_random_alphaNumeric_string
from app.utils.SendMail import SendMail


class LocalesServicios:
    localesDao = LocalesDao()

    def addLocal(self, localJson):
        try:
            usuarioLocalAdmin = UsuarioAdminLocal() \
                .load(localJson)
        except ValidationError as e:
            description = Constantes.COMPLETAR_CAMPOS
            if ("correo" in e.messages):
                description = "Correo erroneo"
            raise CustomException(description=description)

        usuarioLocalAdmin["codigo"] = get_random_alphaNumeric_string()

        usuarioLocalAdmin = self.localesDao.addLocal(usuarioLocalAdmin)

        s = SendMail()
        s.sendMail(usuarioLocalAdmin["correo"], "<html>Bienvenido " + usuarioLocalAdmin["usuario"]
                   + ", te has registrado correctamente.<br><br>"
                   + "Código de invitación: " + usuarioLocalAdmin["codigo"] + "</html>", "BIENVENIDO A APP-LOCAL")

        return usuarioLocalAdmin

    def updateLocal(self, localJson):
        try:
            local = LocalDto() \
                .load(localJson)
        except ValidationError as e:
            description = Constantes.COMPLETAR_CAMPOS
            raise CustomException(description=description)

        local.id_local = localJson["id_local"]
        self.localesDao.updateLocal(local)

        return True

    def getLocal(self, idLocal):
        localDB = self.localesDao.getByIdLocal(idLocal)
        schema = LocalDto()
        return schema.dump(localDB)
