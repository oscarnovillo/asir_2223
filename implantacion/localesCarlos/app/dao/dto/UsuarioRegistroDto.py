from marshmallow import Schema, fields, post_load, validate

from app.dao.modelo.Usuario import Usuario


class UsuarioRegistroDto(Schema):
    admin = fields.Bool()
    usuario = fields.Str(required=True)
    password = fields.Str(required=True)
    correo = fields.Str(required=True, validate=validate.Email, error_messages={"required": "correo invalido"})
    codigo = fields.Str(required=True)
    id_local = fields.Int()

    @post_load
    def make_user(self, data, **kwargs):
        return Usuario(**data)
