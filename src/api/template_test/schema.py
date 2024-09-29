from src.common.utils.ma import ma
from marshmallow import fields
from src.api.question.schema import QuestionSchema
from src.api.alternative.schema import AlternativeSchema

class TemplateTestSchema(ma.Schema):
    id = fields.String()
    name = fields.String()
    author = fields.String()
    description = fields.String()

template_tests_schema = TemplateTestSchema(many=True)

class TemplateTestSelectedSchema(ma.Schema):
    detail = fields.Nested(TemplateTestSchema)
    questions = fields.Nested(QuestionSchema, many=True)
    alternatives = fields.Nested(AlternativeSchema, many=True)
    
template_test_selected_schema = TemplateTestSelectedSchema()