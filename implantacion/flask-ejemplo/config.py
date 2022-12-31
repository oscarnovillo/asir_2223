import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:1asir@informatica.iesquevedo.es:3333/oscar"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
