# ESTO SIRVE PARA CONECTAR LA BASE DE DATOS 
import mysql.connector  # IMPORTAMOS LO QUE HEMOS INSTALADO PIP INSTALL MYSQL.......

database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='bqxo2nyaltlkfb7xfuft-mysql.services.clever-cloud.com',
    port = 3306,
    user ='uzb8hewphwelnsnw', #USUARIO QUE USAMOS NOSOTROS
    password ='YelZ440RYDQGLOlx4leb', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='bqxo2nyaltlkfb7xfuft'
) 

print(database)