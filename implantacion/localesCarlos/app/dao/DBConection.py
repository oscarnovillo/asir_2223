from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO HACE UN SINGLETON y CONFIGURACION


# Define the MySQL engine using MySQL Connector/Python
engine = create_engine(
    'mysql+mysqlconnector://root:root@dam2.mysql.iesquevedo.es:3335/carlosmartin_tfc',
    echo=True)

# Define and create the table
Base = declarative_base()
# El expire_on_commit hace que se puedan deattach los objetos, aunqnue puede dar lecturas sucias.
Session = sessionmaker(bind=engine, expire_on_commit=False)
