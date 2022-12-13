from marshmallow import Schema, fields

class UsuarioGetDto(Schema):
    id_usuario = fields.Int()
    admin = fields.Int()
    usuario = fields.Str()
    url_img =fields.Str()
    correo = fields.Str()
    id_local = fields.Int()
