from src.common.utils.ma import ma
from marshmallow import fields

class PerformanceSchema(ma.Schema):
    question = fields.String()
    answer = fields.String()
    
performance_schema = PerformanceSchema(many=True)