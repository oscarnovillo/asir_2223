from sqlalchemy import Column, String, Integer

from app.dao.DBConection import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(length=200))
    password = Column(String(length=600))
    correo = Column(String(length=200))
    admin =  Column(Integer)
    url_img = Column(String(length=500))
    id_local = Column(Integer)

    # UsuarioRegistroDto
    def __init__(self, usuario, password, id_local=0, admin=False, correo="", **kwargs):
        self.correo = correo
        self.admin = admin
        self.id_local = id_local
        self.usuario = usuario
        self.password = password

    # UsuarioLoginDto
    # def __init__(self,usuario,password):
    #     self.usuario = usuario
    #     self.password = password

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
            self.usuario, self.password, self.correo)
