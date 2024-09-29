from src.common.utils.ma import ma
from marshmallow import fields

class ClasificationSchema(ma.Schema):
    interpretation = fields.String()