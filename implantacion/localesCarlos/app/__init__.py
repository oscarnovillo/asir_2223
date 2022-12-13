from os.path import abspath, dirname, join

from flask import Flask
from flask_mail import Mail
from flask_restful import Api

from app.public.errorHandler.CustomException import CustomException
from app.public.errorHandler.CustomExceptionMapper import \
    handle_custom_exception
from app.public.rest.Eventos import Eventos
from app.public.rest.Locales import Locales, LocalesGet
from app.public.rest.Mejoras import Mejoras, MejorasVoto
from app.public.rest.Recibos import Recibos, RecibosGetLocal, RecibosUtils
from app.public.rest.Usuarios import Usuarios
from app.public.routes.Login import login_api

mail = Mail()


def create_app():
    app = Flask(__name__)
    # necesario para las cookies, hay que generar una.
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/miniblog'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # TODO ponerlo en ficheros configuración bien puestos.
    app.config["DATABASE_URL"] = 'mysql+mysqlconnector://root:root@dam2.mysql.iesquevedo.es:3335/carlosmartin_tfc'
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USERNAME"] = 'alumnosdamquevedo@gmail.com'
    app.config["MAIL_PASSWORD"] = 'ayuaklckgxbbooph'
    app.config["MAIL_FROM"] = 'alumnosdamquevedo@gmail.com'
    app.config["ADMINS"] = ('',)
    app.config["MAIL_USE_TLS"] = True
    app.config["BASE_DIR"] = dirname(dirname(abspath(__file__)))
    app.config["PATH_IMG_PROFILE"] = join(dirname(dirname(abspath(__file__))), "images")
    app.config["URL_IMG_PROFILE"] = "images/"
    app.config["PATH_PDF"] = join(dirname(dirname(abspath(__file__))), "recibos")
    app.config["URL_PDF"] = "recibos/"

    api = Api(app, prefix="/api")
    api.add_resource(Usuarios, '/usuarios')
    api.add_resource(Locales, '/locales')
    api.add_resource(Recibos, '/recibos')
    api.add_resource(Mejoras, '/mejoras')
    api.add_resource(MejorasVoto, '/mejoras/votar')
    api.add_resource(Eventos, '/eventos')
    api.add_resource(LocalesGet, '/locales/<int:idLocal>')
    api.add_resource(RecibosGetLocal, '/recibos/recibosLocal')
    api.add_resource(RecibosUtils, '/recibos/recibosUtils')

    app.register_blueprint(login_api)
    app.register_error_handler(CustomException, handle_custom_exception)
    app.register_error_handler(500, handle_custom_exception)

    mail.init_app(app)

    return app

