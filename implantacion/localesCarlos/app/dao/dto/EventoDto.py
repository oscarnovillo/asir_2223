from marshmallow import Schema, fields, validate, post_load

from app.dao.modelo.Evento import Evento


class EventoDto(Schema):
    id = fields.Int()

    id_local = fields.Int()
    id_usuario = fields.Int()
    titulo = fields.Str(required=True \
                        , validate=validate.Length(min=1), error_messages={"required": "nombre required"})
    descripcion = fields.Str(required=True \
                             , validate=validate.Length(min=1), error_messages={"required": "nombre required"})

    latitud = fields.Float()
    longitud = fields.Float()
    url_img = fields.Str()
    fecha = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return Evento(**data)
