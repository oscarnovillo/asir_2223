from sqlalchemy import Column, Integer, String, DateTime, Float

from app.dao.DBConection import Base


class Recibo(Base):
    __tablename__ = 'recibos'

    id_recibo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_usuario = Column(Integer)
    id_local = Column(Integer)
    importe = Column(Float)
    descripcion = Column(String(length=500))
    fecha = Column(DateTime)
    id_tipo_gasto = Column(Integer)
    url_pdf = Column(String(length=200))

    def __init__(self, id_usuario, id_local, importe, descripcion, fecha,
                 id_tipo_gasto, url_pdf, **kwargs):
        self.id_usuario = id_usuario
        self.id_local = id_local
        self.importe = importe
        self.descripcion = descripcion
        self.fecha = fecha
        self.id_tipo_gasto = id_tipo_gasto
        self.url_pdf = url_pdf
