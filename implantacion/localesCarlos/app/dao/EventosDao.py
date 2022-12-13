from app.dao.DBConection import Session
from app.dao.modelo.Evento import Evento


class EventosDao:

    def addEvento(self, evento):
        session = Session()
        session.add(evento)
        session.commit()
        return True

    def obtenerEventosPorIdLocal(self, idLocal):
        session = Session()

        eventosDb = session.query(Evento).filter_by(id_local=idLocal).all()

        session.close()

        return eventosDb

    def deleteEvento(self, idEvento):
        try:
            session = Session()

            filasBorradas = session.query(Evento).filter_by(id=idEvento).delete()

            session.commit()
        finally:
            session.close()

        return True
