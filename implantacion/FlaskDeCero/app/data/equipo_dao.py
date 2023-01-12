
from app.data.modelo.equipo import Equipo

class EquipoDao:

    def select_all(self,db) -> list[Equipo]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM equipos')
        equipos_en_db = cursor.fetchall()
        equipos : list[Equipo]= list()
        for equipo_en_db in equipos_en_db:
            equipos.append(Equipo(equipo_en_db[0], equipo_en_db[1], equipo_en_db[2]))

        cursor.close()
        return equipos