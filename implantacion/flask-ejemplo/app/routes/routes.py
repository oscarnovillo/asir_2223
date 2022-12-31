from flask import Blueprint, render_template, request

from app import db
from app.data.modelo.user import User
from app.servicios.userServicios import UserServicios

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        param = request.form["q"]
        return render_template("post.html", parametro=param)
    else:
        return render_template("index.html")


@bp.route("/verTodos")
def ver_todos():
    user_services = UserServicios(db)
    return render_template("listado.html", usuarios=user_services.get_all())


@bp.route("/verUno")
def ver_uno():
    id_usuario: int = request.args.get("id", default=0, type=int)
    user_services = UserServicios(db)
    return render_template(
        "usuario.html", user=user_services.get_user_by_id(id_usuario)
    )


@bp.route("/add")
def add_user():
    nombre: str = request.args.get("nombre", default="", type=str)
    apellidos: str = request.args.get("apellido", default="", type=str)
    user_services = UserServicios(db)
    user = User(username=nombre, password=apellidos)
    return render_template("usuario.html", user=user_services.add_user(user))
