from sqlalchemy import Column, Integer, String, Float

from app.dao.DBConection import Base


class Local(Base):
    __tablename__ = 'locales'

    id_local = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(length=200))
    direccion = Column(String(length=500))
    capital = Column(Float)
    cuota = Column(Float)
    codigo = Column(String(length=10))

    def __init__(self, nombre, direccion, capital, cuota, codigo, **kwargs):
        # if (id_local != 0):
        #     self.id_local = id_local

        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.cuota = cuota
        self.capital = capital
