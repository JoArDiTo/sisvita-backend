from src.common.utils.ma import ma
from marshmallow import fields
from src.api.answer.schema import PerformanceSchema

class TestSchema(ma.Schema):
    id = fields.String()
    template_test_name = fields.String()
    template_test_author = fields.String()
    date = fields.DateTime(required=True)
    interpretation = fields.String()

tests_schema = TestSchema(many=True)

class TestDetailSchema(ma.Schema):
    test = fields.Nested(TestSchema)
    performance = fields.Nested(PerformanceSchema, many=True)
    
test_detail_schema = TestDetailSchema()