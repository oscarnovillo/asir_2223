from flask import current_app
from flask_mail import Message


# Configuración del email
# from app import mail


class SendMail:

    # TODO MANDAR MAIL ASINCRONO
    def sendMail(self, toMail, html, subject):
        msg = Message(html=html,
                      sender=current_app.config["MAIL_FROM"],
                      recipients=[toMail],
                      subject=subject)
        from app import mail
        mail.send(msg)
