from sqlalchemy import Column, Integer, String

from app.dao.DBConection import Base


class Votacion(Base):
    __tablename__ = 'votaciones'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_mejora = Column(Integer)
    id_usuario = Column(Integer)
    decision = Column(String(length=2))

    def __init__(self, id_mejora, id_usuario, decision, **kwargs):
        self.id_mejora = id_mejora
        self.id_usuario = id_usuario
        self.decision = decision
