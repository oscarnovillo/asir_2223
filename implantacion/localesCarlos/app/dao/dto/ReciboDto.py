from marshmallow import Schema, fields, validate, post_load

from app.dao.modelo.Recibo import Recibo


class ReciboDto(Schema):

    id_recibo = fields.Int()
    id_usuario = fields.Int()
    id_local = fields.Int()
    importe = fields.Float()
    descripcion = fields.Str(required=True \
                             , validate=validate.Length(min=1), error_messages={"required": "descripcion required"})
    fecha = fields.DateTime()
    id_tipo_gasto = fields.Int()
    url_pdf = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return Recibo(**data)
