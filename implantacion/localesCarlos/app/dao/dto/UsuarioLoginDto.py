from marshmallow import Schema, fields, post_load, validate

from app.dao.modelo.Usuario import Usuario


class UsuarioLoginDto(Schema):

    usuario = fields.Str(required=True)
    password = fields.Str(required=True \
                          , validate=validate.Length(min=1),error_messages={"required": "password required"})

    @post_load
    def make_user(self, data, **kwargs):
        return Usuario(**data)