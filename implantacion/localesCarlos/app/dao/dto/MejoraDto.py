from marshmallow import Schema, fields, validate, post_load

from app.dao.modelo.Mejora import Mejora


class MejoraDto(Schema):
    id = fields.Int()

    id_local = fields.Int()
    id_usuario = fields.Int()
    titulo = fields.Str(required=True \
                        , validate=validate.Length(min=1), error_messages={"required": "nombre required"})
    descripcion = fields.Str(required=True \
                             , validate=validate.Length(min=1), error_messages={"required": "nombre required"})
    url_img = fields.Str()
    importe = fields.Float()
    votos_positivos = fields.Int()
    votos_negativos = fields.Int()
    estado = fields.Str()
    voto = fields.Str()
    votada = fields.Bool()

    @post_load
    def make_user(self, data, **kwargs):
        return Mejora(**data)
