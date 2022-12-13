from sqlalchemy.exc import IntegrityError

from app.dao.DBConection import Session
from app.dao.modelo.Local import Local
from app.dao.modelo.Usuario import Usuario
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes
from app.utils.PasswordHash import PasswordHash


class LocalesDao:

    def getByCodigo(self, codigo):
        session = Session()

        localDb = session.query(Local).filter_by(codigo=codigo).first()

        session.close()

        return localDb

    def getByIdLocal(self, idLocal):
        session = Session()

        localDb = session.query(Local).filter_by(id_local=idLocal).first()

        session.close()

        return localDb

    def addLocal(self, usuarioAdminLocal):
        session = Session()
        local = Local(**usuarioAdminLocal)
        usuario = Usuario(**usuarioAdminLocal)

        ph = PasswordHash()
        usuario.password = ph.hashPassword(usuario.password)
        usuario.admin = True

        try:
            session.add(local)
            session.flush()
        except IntegrityError as e:
            session.rollback()
            if "locales_nombre_uindex" in e._message():
                raise CustomException(Constantes.LOCAL_EXISTENTE)
            else:
                raise CustomException(Constantes.LOCAL_EXISTENTE)

        try:
            usuario.id_local = local.id_local
            session.add(usuario)
            usuarioAdminLocal["id_local"] = local.id_local
            session.commit()
        except IntegrityError as e:
            session.rollback()
            if "usuarios_correo_uindex" in e._message():
                raise CustomException(Constantes.CORREO_EXISTENTE)
            else:
                raise CustomException(Constantes.USUARIO_EXISTENTE)
            raise CustomException(description=Constantes.CODIGO_LOCAL_ERRONEO)

        session.close()

        return usuarioAdminLocal

    def updateLocal(self, local):
        session = Session()
        try:
            localDb = session.query(Local).get(local.id_local)
            localDb.nombre = local.nombre
            localDb.direccion = local.direccion
            localDb.cuota = local.cuota
            session.commit()
        except IntegrityError as e:
            session.rollback()
            if "locales_nombre_uindex" in e._message():
                raise CustomException(Constantes.LOCAL_EXISTENTE)
            else:
                raise CustomException(Constantes.LOCAL_EXISTENTE)
        session.close()
        return True
