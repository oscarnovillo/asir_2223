import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://:password@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
