from marshmallow import Schema, fields, validate


class UsuarioAdminLocal(Schema):
    id_local = fields.Int()
    nombre = fields.Str(required=True \
                        , validate=validate.Length(min=1), error_messages={"required": "nombre required"})

    direccion = fields.Str(required=True \
                           , validate=validate.Length(min=1), error_messages={"required": "direccion required"})

    capital = fields.Float()
    cuota = fields.Float()
    codigo = fields.Str()
    usuario = fields.Str(required=True \
                         , validate=validate.Length(min=1), error_messages={"required": "usuario required"})

    password = fields.Str(required=True \
                          , validate=validate.Length(min=1), error_messages={"required": "password required"})

    correo = fields.Str(required=True \
                        , validate=validate.Email(), error_messages={"required": "correo invalido"})

    codigo = fields.Str()
