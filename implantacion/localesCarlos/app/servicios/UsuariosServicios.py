import os

from flask_api import status
from marshmallow import ValidationError
from werkzeug.utils import secure_filename

from app.dao.LocalesDao import LocalesDao
from app.dao.UsuariosDao import UsuariosDao
from app.dao.dto.UsuarioGetDto import UsuarioGetDto
from app.dao.dto.UsuarioLoginDto import UsuarioLoginDto
from app.dao.dto.UsuarioRegistroDto import UsuarioRegistroDto
from app.public.errorHandler.CustomException import CustomException
from app.utils.Constantes import Constantes
from app.utils.PasswordHash import PasswordHash
from app.utils.SendMail import SendMail


class UsuariosServicios:

    def getAllUsuarios(self):
        usuariosDao = UsuariosDao()
        usuarios = usuariosDao.getAll()
        schema = UsuarioGetDto(many=True)
        return schema.dump(usuarios)

    def login(self, usuarioJson):
        try:
            usuario = UsuarioLoginDto() \
                .load(usuarioJson)
        except ValidationError as e:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS, code=status.HTTP_400_BAD_REQUEST)

        usuariosDao = UsuariosDao()

        usuarioDB = usuariosDao.getByUsername(usuario.usuario)
        if (usuarioDB is None):
            raise CustomException(description=Constantes.USUARIO_NO_EXISTE, code=status.HTTP_403_FORBIDDEN)
        # comprobar contraseña
        ph = PasswordHash()

        if not ph.checkPassword(usuario.password, usuarioDB.password):
            raise CustomException(description=Constantes.PASSWORD_INCORRECTA, code=status.HTTP_403_FORBIDDEN)

        schema = UsuarioGetDto()
        return schema.dump(usuarioDB)

    def getUsuariosByIdLocal(self, idLocal):
        usuariosDao = UsuariosDao()
        usuarios = usuariosDao.getByLocal(idLocal)
        schema = UsuarioGetDto(many=True)
        return schema.dump(usuarios)

    def addUsuario(self, usuarioJson):
        try:
            usuario = UsuarioRegistroDto() \
                .load(usuarioJson)
        except ValidationError as e:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)

        localesDao = LocalesDao()
        local = localesDao.getByCodigo(usuarioJson['codigo'])
        if local is None:
            raise CustomException(description=Constantes.CODIGO_LOCAL_ERRONEO)

        usuario.id_local = local.id_local
        ph = PasswordHash()
        usuario.password = ph.hashPassword(usuario.password)

        usuariosDao = UsuariosDao()

        usuario = usuariosDao.saveUsuario(usuario)

        s = SendMail()
        s.sendMail(usuario.correo, "<html>Bienvenido " + usuario.usuario
                   + ", te has registrado correctamente.</html>", "BIENVENIDO A APP-LOCAL")
        schema = UsuarioGetDto()
        return schema.dump(usuario)

    def updateUsuario(self, usuarioJson, idUsuario):
        try:
            usuario = UsuarioRegistroDto() \
                .load(usuarioJson)
        except ValidationError as e:
            raise CustomException(description=Constantes.COMPLETAR_CAMPOS)
        usuario.id_usuario = idUsuario

        usuariosDao = UsuariosDao()
        usuariosDao.updateUsuario(usuario)

    def recoveryPassword(self, recovery):
        usuariosDao = UsuariosDao()

        usuarioDb = usuariosDao.recoveryPass(recovery)

        if usuarioDb is not None:
            s = SendMail()
            s.sendMail(usuarioDb.correo, "<html>Su nombre de usuario: " + usuarioDb.usuario + "<br><br>" +
                       "Su nueva contraseña: " + usuarioDb.password + " </html>", "RECUPERACION")
            return True
        return False

    def addPhotoUsuario(self, images_dir, url_path, file, idUsuario):

        image_name = secure_filename(file.filename)
        os.makedirs(images_dir, exist_ok=True)
        file_path = os.path.join(images_dir, image_name)
        file.save(file_path)
        usuariosDao = UsuariosDao()
        usuariosDao.addPhotoUsuario(url_path + image_name, idUsuario)
        return url_path + image_name
