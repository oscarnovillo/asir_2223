import datetime

from sqlalchemy import and_
from app.dao.DBConection import Session
from app.dao.modelo.Local import Local
from app.dao.modelo.Recibo import Recibo


class RecibosDao:

    def addRecibo(self, recibo):
        try:
            session = Session()
            session.add(recibo)
            session.flush()
            localDb = session.query(Local).get(recibo.id_local)
            localDb.capital = localDb.capital + recibo.importe
            session.commit()
            return localDb
        finally:
            session.close()

    def getRecibosUsuarios(self, id):
        session = Session()
        recibosDb = session.query(Recibo).filter_by(id_usuario=id).all()
        session.close()
        return recibosDb

    def getRecibosLocal(self, id):
        session = Session()
        recibosDB = session.query(Recibo).filter_by(id_local=id).all()
        session.close()
        return recibosDB

    def verificarPago(self, idLocal, idUser):
        session = Session()
        actual = datetime.datetime.now()
        inicial = datetime.datetime(actual.year, actual.month, 1)
        reciboDB = session.query(Recibo).filter_by(id_local=idLocal, id_usuario=idUser).filter(
            Recibo.fecha.between(inicial, actual)).first()
        session.close()
        return reciboDB

    def addJustificante(self, recibo):
        session = Session()
        reciboDB = session.query(Recibo).filter_by(id_recibo=recibo.id_recibo).first()
        reciboDB.url_pdf = recibo.url_pdf
        session.commit()
        return reciboDB.url_pdf

    def deleteRecibo(self, id):
        try:
            session = Session()
            reciboDB = session.query(Recibo).filter_by(id_recibo=id).first()
            localDB = session.query(Local).filter_by(id_local=reciboDB.id_local).first()
            localDB.capital = localDB.capital - reciboDB.importe
            session.query(Recibo).filter_by(id_recibo=reciboDB.id_recibo).delete()
            session.commit()
            return localDB.capital
        finally:
            session.close()
