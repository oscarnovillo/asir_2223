from functools import wraps

from flask import session, abort

from app.utils.Constantes import Constantes


def filterLogin(f):
    @wraps(f)
    def cacher(*args, **kwargs):
        if Constantes.SESSION_LOGIN not in session or session[Constantes.SESSION_LOGIN] != 'ok':
            abort(403)
        return f(*args, **kwargs)

    return cacher
