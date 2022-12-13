from sqlalchemy import Column, Integer, DateTime, String, Float

from app.dao.DBConection import Base


class Evento(Base):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_local = Column(Integer)
    id_usuario = Column(Integer)
    titulo = Column(String(length=200))
    descripcion = Column(String(length=500))
    latitud = Column(Float)
    longitud = Column(Float)
    url_img = Column(String(length=500))
    fecha = Column(DateTime)

    def __init__(self, id_local, id_usuario, titulo, descripcion, latitud, longitud, fecha, url_img="", **kwargs):
        self.titulo = titulo
        self.id_usuario = id_usuario
        self.id_local = id_local
        self.descripcion = descripcion
        self.latitud = latitud
        self.longitud = longitud
        self.url_img = url_img
        self.fecha = fecha
