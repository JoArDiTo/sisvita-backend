from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import TemplateTest
from src.api.question.models import Question
from src.api.alternative.models import Alternative
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import template_tests_schema, template_test_selected_schema
from src.api.question.schema import questions_schema
from src.api.alternative.schema import alternatives_schema

template_tests = Blueprint('template_tests', __name__)

@template_tests.route('/add', methods=['POST'])
def addTemplateTest():
    name = data().get('name')
    author = data().get('author')
    description = data().get('description')
    
    if not name or not author or not description:
        return make_response(jsonify({'message': 'All fields are required'}), 400)
    
    template_test = TemplateTest.query.filter_by(name=name).first()
    if template_test:
        return make_response(jsonify({'message': 'Template test already registered'}), 400)
    
    new_template_test = TemplateTest(name, author, description)
    db.session.add(new_template_test)
    db.session.commit()
    
    return make_response(jsonify({
        'message': 'Template test registered successfully',
        'id': new_template_test.id
    }), 201)
    
@template_tests.route('/get', methods=['GET'])
def getTemplateTests():
    template_tests = TemplateTest.query.all()
    return make_response(template_tests_schema.jsonify(template_tests), 200)

@template_tests.route('/get/<string:id>', methods=['GET'])
#@jwt_required()
def getTemplateTest(id):
    template_test = TemplateTest.query.filter_by(id=id).first()
    if not template_test:
        return make_response(jsonify({'message': 'Template test not found'}), 404)
    
    questions = Question.query.filter_by(template_test_id=id).all()
    alternatives = Alternative.query.filter_by(template_test_id=id).all()
    
    template_test_selected = template_test_selected_schema.dump({
        'detail': template_test,
        'questions': questions_schema.dump(questions),
        'alternatives': alternatives_schema.dump(alternatives)
    })
    
    return make_response(jsonify({
        'template_test': template_test_selected
    }), 200)