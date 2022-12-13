from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.elements import or_

from app.dao.DBConection import Session
from app.dao.modelo.Usuario import Usuario
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes
from app.utils.PasswordHash import PasswordHash, get_random_alphaNumeric_string


class UsuariosDao:

    def getAll(self):
        session = Session()

        usuariosDb = session.query(Usuario).all()

        # serializing as JSON
        session.close()

        return usuariosDb

    def getByLocal(self, idLocal):
        session = Session()

        usuariosDb = session.query(Usuario).filter_by(id_local=idLocal).all()

        # serializing as JSON
        session.close()

        return usuariosDb

    def getByUsername(self, userName):
        session = Session()

        usuariosDb = session.query(Usuario).filter_by(usuario=userName).first()

        session.close()

        return usuariosDb

    def saveUsuario(self, usuario):
        session = Session()
        try:
            session.add(usuario)
            session.commit()
        except IntegrityError as e:
            if "usuarios_correo_uindex" in e._message():
                raise CustomException(Constantes.CORREO_EXISTENTE)
            else:
                raise CustomException(Constantes.USUARIO_EXISTENTE)
            raise CustomException(description=Constantes.CODIGO_LOCAL_ERRONEO)

        session.close()
        return usuario

    def updateUsuario(self, usuario):
        session = Session()
        try:
            ph = PasswordHash()
            usuarioDb = session.query(Usuario).get(usuario.id_usuario)
            if usuario.password != "********":
                usuarioDb.password = ph.hashPassword(usuario.password)
            usuarioDb.usuario = usuario.usuario
            usuarioDb.correo = usuario.correo
            session.commit()
        except IntegrityError as e:
            if "usuarios_correo_uindex" in e._message():
                raise CustomException(Constantes.CORREO_EXISTENTE)
            else:
                raise CustomException(Constantes.USUARIO_EXISTENTE)
            raise CustomException(description=Constantes.CODIGO_LOCAL_ERRONEO)
        session.close()

    def addPhotoUsuario(self, file_path, id_usuario):
        session = Session()
        usuarioDb = session.query(Usuario).get(id_usuario)
        usuarioDb.url_img = file_path
        session.commit()
        session.close()

    def recoveryPass(self, recovery):

        session = Session()

        ph = PasswordHash()
        passwordNueva = get_random_alphaNumeric_string()
        usuarioDb = session.query(Usuario).filter(or_(Usuario.usuario == recovery, Usuario.correo == recovery)).first()
        if usuarioDb is not None:
            numFilas = session.query(Usuario).filter_by(id_usuario=usuarioDb.id_usuario).update(
                {Usuario.password: ph.hashPassword(passwordNueva)})
            session.commit()
            usuarioDb.password = passwordNueva

        session.close()
        return usuarioDb
