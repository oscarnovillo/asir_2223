from marshmallow import Schema, fields, validate, post_load

from app.dao.modelo.Local import Local


class LocalDto(Schema):
    id_local = fields.Int()
    nombre = fields.Str(required=True \
                        , validate=validate.Length(min=1), error_messages={"required": "nombre required"})

    direccion = fields.Str(required=True \
                           , validate=validate.Length(min=1), error_messages={"required": "direccion required"})

    capital = fields.Float()
    cuota = fields.Float()
    codigo = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return Local(**data)
