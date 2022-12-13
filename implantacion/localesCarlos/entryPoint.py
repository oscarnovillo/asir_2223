# from flask import Flask,g
# from flask_mail import Mail, Message
# from flask_restful import Api
#
# from app.public.errorHandler.CustomException import CustomException
# from app.public.errorHandler.CustomExceptionMapper import handle_custom_exception
# from app.public.rest.Usuarios import Usuarios
# from app.public.routes.Login import login_api
#
# app = Flask(__name__)
# # necesario para las cookies, hay que generar una.
# app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"
# app.register_blueprint(login_api)
# app.register_error_handler(CustomException, handle_custom_exception)
#
# app.config["MAIL_SERVER"] = 'smtp.gmail.com'
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_USERNAME"] = 'app.local.tfc@gmail.com'
# app.config["MAIL_PASSWORD"] = 'applocal2020'
# app.config["MAIL_FROM"] = 'app.local.tfc@gmail.com'
# app.config["ADMINS"] = ('juanjo@j2logo.com',)
# app.config["MAIL_USE_TLS"] = True
#
#
# api = Api(app,prefix="/api")
# api.add_resource(Usuarios, '/usuarios')
# mail = Mail()
# mail.init_app(app)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
