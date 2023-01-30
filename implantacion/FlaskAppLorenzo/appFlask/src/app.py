from flask import Flask, render_template, request, redirect, url_for
import os  # PARA PODER ACCEDER A LOS DIRECTORIOS DE UNA MANERA FÁCIL 
import database as db # IMPORTAMOS EL ARCHIVO DATABASE PARA PODER ACCEDER A LA BASE DE DATOS

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # ESTO NOS SIRVE PARA ACCEDER A LA CARPETA DEL PROYECTO ABSOLUTO
template_dir = os.path.join(template_dir,'src','templates') # ESTO SIRVE PARA UNIR LA CARPETA SRC Y TEMPLATES AL PROYECTO

app = Flask(__name__, template_folder = template_dir) # ESTO ES PARA INICIAR LA APLICACIÓN, EL TEMPLATE_FOLDER ES LA DIRECCION QUE INDICAMOS ANTES



# RUTAS DE LA APLICACIÓN 

@app.route('/')  # ESTO ES LA RUTA PRINCIPAL DE NUESTRA APP SE PONE CON LA BARRA
def home():
    cursor = db.database.cursor() # PARA ACCEDER A LA BD
    cursor.execute("SELECT * FROM InformacionAlumno") # PARA OBTENER TODOS LOS DATOS DE LA BD QUE VAMOS A VER EN NUESTRO INDEX
    myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
    #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
    insertObject = [] # AQUI VAN GUARDADAS LAS CLAVES DE LAS COLUMNAS
    columnNames = [column[0] for column in cursor.description] # PARA OBTENER LOS NOMBRES DE LAS COLUMNAS
    for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
        insertObject.append(dict(zip(columnNames,record))) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
    cursor.close() # PARA CERRAR EL CURSOR

    return render_template('index.html', data=insertObject)  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML

#INDICAMOS EL NOMBRE DE LA RUTA GUARDAR USUARIOS EN LA BASE DE DATOS
@app.route('/user', methods=['POST'])
def addUser():
    Nombre = request.form['Nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    Apellido = request.form['Apellido'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS
    CentroFormativo = request.form['CentroFormativo'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS

    if Nombre and Apellido and CentroFormativo: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "INSERT INTO InformacionAlumno (Nombre,Apellido,CentroFormativo) VALUES (%s, %s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = (Nombre,Apellido,CentroFormativo) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK

@app.route('/delete/<string:CodigoAlumno>')
def delete(CodigoAlumno):
    cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
    sql = "DELETE FROM InformacionAlumno WHERE CodigoAlumno=%s"
    data = (CodigoAlumno,) # HACEMOS UNA TUPLA CON LOS DATOS 
    cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
    db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@app.route('/edit/<string:CodigoAlumno>', methods=['POST'])
def edit (CodigoAlumno):
    Nombre = request.form['Nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE DE USUARIO QUE INDIQUEMOs
    Apellido = request.form['Apellido'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    CentroFormativo = request.form['CentroFormativo'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS

    if Nombre and Apellido and CentroFormativo: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "UPDATE InformacionAlumno SET Nombre = %s, Apellido = %s, CentroFormativo = %s WHERE CodigoAlumno = %s"# DEFINIMOS LA CONSULTA UPDATE EN LOS SIGUIENTES CAMPOS
        data = (Nombre,Apellido,CentroFormativo,CodigoAlumno) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK



####################################################### NOTAS ################################################################

class Alumno:
        def __init__(self, CodigoAlumno, Nombre):
            self.CodigoAlumno = CodigoAlumno
            self.Nombre = Nombre


@app.route('/notas')  # ESTO ES LA RUTA PARA VER LAS NOTAS DE LOS ALUMNOS EN MI APP SE PONE CON LA BARRA
def notas():
    cursor = db.database.cursor() # PARA ACCEDER A LA BD
    cursor.execute("SELECT i.Nombre,n.CodigoAlumno,n.Seguridad,n.Implantacion,n.Redes FROM Notas n INNER JOIN InformacionAlumno i on n.CodigoAlumno = i.CodigoAlumno") # PARA OBTENER TODOS LOS DATOS DE LA BD QUE VAMOS A VER EN NUESTRO INDEX
    myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
    #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
    insertObject = [] # AQUI VAN GUARDADAS LAS CLAVES DE LAS COLUMNAS
    columnNames = [column[0] for column in cursor.description] # PARA OBTENER LOS NOMBRES DE LAS COLUMNAS
    for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
        insertObject.append(dict(zip(columnNames,record))) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
    cursor.close() # PARA CERRAR EL CURSOR


    cursor = db.database.cursor() # PARA ACCEDER A LA BD
    cursor.execute("""SELECT i.CodigoAlumno,i.Nombre 
    FROM Notas n RIGHT JOIN InformacionAlumno i on n.CodigoAlumno = i.CodigoAlumno
    where n.CodigoAlumno is null""") 

    myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
    alumnosSinNotas : Alumno = []
    #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
    for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
        alumnosSinNotas.append(Alumno(record[0],record[1])) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
    cursor.close() #



    return render_template('notas.html', notasAlumnos=insertObject,alumnosSinNotas = alumnosSinNotas)  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML

#INDICAMOS EL NOMBRE DE LA RUTA GUARDAR USUARIOS EN LA BASE DE DATOS
@app.route('/userNotas', methods=['POST'])
def addNotas():
    CodigoAlumno = request.form['CodigoAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL CODIGO ALUMNO QUE INDIQUEMOS
    Seguridad = request.form['Seguridad'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
    Implantacion = request.form['Implantacion'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
    Redes = request.form['Redes'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS

    if CodigoAlumno and Seguridad and Implantacion and Redes: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "INSERT INTO Notas (CodigoAlumno,Seguridad,Implantacion,Redes) VALUES (%s, %s, %s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
        data = (CodigoAlumno,Seguridad,Implantacion,Redes) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK

@app.route('/deleteNotas/<string:CodigoAlumno>')
def deleteNotas(CodigoAlumno):
    cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
    sql = "DELETE FROM Notas WHERE CodigoAlumno=%s"
    data = (CodigoAlumno,) # HACEMOS UNA TUPLA CON LOS DATOS 
    cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
    db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK

########### A LA HORA DE BORRAR UN ALUMNO SE NOS BORRARÁN LAS NOTAS TAMBIEN POR LA FORANEA CODIGO ALUMNO ON UPDATE CASCADE ON DELETE CASCADE #################

@app.route('/editNotas/<string:CodigoAlumno>', methods=['POST'])
def editNotas (CodigoAlumno):
    CodigoAlumno = request.form['CodigoAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL CodigoAlumno QUE INDIQUEMOS
    Seguridad = request.form['Seguridad'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA DE SEGURIDAD QUE INDIQUEMOS
    Implantacion = request.form['Implantacion'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON CON LA NOTA DE IMPLANTACION QUE INDIQUEMOS
    Redes = request.form['Redes'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA DE REDES QUE INDIQUEMOS

    if CodigoAlumno and Seguridad and Implantacion and Redes: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
        cursor = db.database.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "UPDATE Notas SET Seguridad = %s, Implantacion = %s, Redes = %s WHERE CodigoAlumno = %s"# DEFINIMOS LA CONSULTA UPDATE EN LOS SIGUIENTES CAMPOS
        data = (Seguridad,Implantacion,Redes,CodigoAlumno) # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        db.database.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
    return redirect(url_for('notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK



if __name__ == '__main__':
    app.run(debug=True,port=80,host="0.0.0.0") # ESTO SIRVE PARA PONER EL MODO DEBUG EN ON Y NO TENER QUE ESTAR CERRANDO Y ABRIENDO EL SERVIDOR. LO INICIALIZO EN EL PUERTO 4000 PARA PROBAR.

