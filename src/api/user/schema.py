from src.common.utils.ma import ma
from marshmallow import fields

class ProfileSchema(ma.Schema):
    document_type = fields.String(required=True)
    document_number = fields.String(required=True)
    first_name = fields.String(required=True)
    paternal_surname = fields.String(required=True)
    maternal_surname = fields.String(required=True)
    phone_number = fields.String(required=True)
    email = fields.String(required=True)
    
user_schema = ProfileSchema()