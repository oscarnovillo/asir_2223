
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.data.modelo import Base


class Moto(Base):
    __tablename__ = 'motos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    
 