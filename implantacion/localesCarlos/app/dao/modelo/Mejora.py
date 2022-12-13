from sqlalchemy import Column, Integer, String, Float

from app.dao.DBConection import Base


class Mejora(Base):
    __tablename__ = 'mejoras'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_local = Column(Integer)
    id_usuario = Column(Integer)
    titulo = Column(String(length=100))
    descripcion = Column(String(length=500))
    url_img = Column(String(length=500))
    importe = Column(Float)
    votos_positivos = Column(Integer)
    votos_negativos = Column(Integer)
    estado = Column(String(length=500))

    def __init__(self, id_local, id_usuario, titulo, descripcion, importe, url_img="", votosNegativos=0,
                 votosPositivos=0, estado='', **kwargs):
        self.id_local = id_local
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.descripcion = descripcion
        self.importe = importe
        self.votos_negativos = votosNegativos
        self.votos_positivos = votosPositivos
        self.url_img = url_img
        self.estado = estado
