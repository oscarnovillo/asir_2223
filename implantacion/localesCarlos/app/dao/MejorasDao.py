from sqlalchemy import text

from app.dao.DBConection import Session, engine
from app.dao.modelo.Mejora import Mejora
from app.dao.modelo.Usuario import Usuario


class MejorasDao:

    def addMejora(self, mejora):
        session = Session()
        session.add(mejora)
        session.commit()
        session.close()
        return True

    def deleteEvento(self, idMejora):
        try:
            session = Session()

            filasBorradas = session.query(Mejora).filter_by(id=idMejora).delete()

            session.commit()
        finally:
            session.close()

        return True

    def addVoto(self, mejora, votacion):
        try:
            session = Session()
            numUsers = session.query(Usuario).filter_by(id_local=mejora.id_local).count()
            mejoraDb = session.query(Mejora).filter_by(id=mejora.id).first()
            mejoraDb.estado = self.__checkEstadoVotacion(mejora, numUsers)
            mejoraDb.votos_negativos = mejora.votos_negativos
            mejoraDb.votos_positivos = mejora.votos_positivos
            session.add(votacion)
            session.commit()
        finally:
            session.close()

        return True

    def obtenerMejoras(self, idLocal, idUsuario, estado):
        try:
            con = engine.connect()
            stmt = text("""select m.*,IF(v.id is null,FALSE,TRUE) as votada from mejoras m left join 
                        (select * from votaciones v where id_usuario=:id_usuario) v on m.id = v.id_mejora 
                        where id_local = :id_local and estado=:estado""")
            result = con.execute(stmt, id_usuario=idUsuario, id_local=idLocal, estado=estado)
            mejoras = []
            for row in result:
                mejoras.append(row)

        finally:
            con.close()

        return mejoras

    def __checkEstadoVotacion(self, mejora, numUsers):
        if mejora.votos_positivos > numUsers / 2:
            return "APROBADAS"
        elif mejora.votos_negativos > numUsers / 2:
            return "RECHAZADAS"
        elif mejora.votos_negativos == numUsers / 2 and mejora.votos_positivos == numUsers / 2:
            return "RECHAZADAS"

        return "EN VOTACION"
