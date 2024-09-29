from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Test
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import tests_schema, test_detail_schema
from src.api.template_test.models import TemplateTest
from src.api.clasification.models import Clasification
from src.api.question.models import Question
from src.api.alternative.models import Alternative
from src.api.answer.models import Answer

tests = Blueprint('tests', __name__)

@tests.route('/add/<string:template_test_id>', methods=['POST'])
@jwt_required()
def addTest(template_test_id):
    current_user_id = get_jwt_identity()
    values = data().get('values')
    score = 0
    for value in values:
        score += value
    print(score)
        
    clasification_id = Clasification.query.filter(
        Clasification.template_test_id == template_test_id,
        Clasification.min_score<=score,
        Clasification.max_score>=score
    ).first().id
    
    test = Test(score, clasification_id, template_test_id, current_user_id)
    db.session.add(test)
    db.session.commit()
    
    return make_response(jsonify({
        'message': 'Test registered successfully',
        'id': test.id
    }), 201)
    
@tests.route('/get', methods=['GET'])
@jwt_required()
def getTestByUser():
    current_user_id = get_jwt_identity()
    tests = Test.query.filter_by(user_id=current_user_id).all()
    
    if not tests:
        return make_response(jsonify({
            'message': 'Tests not founded'
        }), 404)
    
    tests_dto = []
    
    for test in tests:
        tests_dto.append({
            'id': test.id,
            'template_test_name': TemplateTest.query.get(test.template_test_id).name,
            'template_test_author': TemplateTest.query.get(test.template_test_id).author,
            'date': test.date,
            'interpretation': Clasification.query.get(test.clasification_id).interpretation
        })
    
    return make_response(jsonify({
        'message': 'Tests founded successfully',
        'tests': tests_schema.dump(tests_dto)
    }), 200)
    
@tests.route('/get/<string:test_id>', methods=['GET'])
@jwt_required()
def getTestDetail(test_id):
    test = Test.query.get(test_id)
    
    test_dto = {
        'id': test.id,        
        'template_test_name': TemplateTest.query.get(test.template_test_id).name,
        'template_test_author': TemplateTest.query.get(test.template_test_id).author,
        'date': test.date,
        'interpretation': Clasification.query.get(test.clasification_id).interpretation
    }
    
    performance = []
    answers = Answer.query.filter_by(test_id=test_id).all()
    for answer in answers:
        performance.append({
            'question': Question.query.get(answer.question_id).content,
            'answer': Alternative.query.get(answer.alternative_id).content,
        })
    
    return make_response(jsonify({
        'message': 'Test founded successfully',
        'test': test_detail_schema.dump({'test': test_dto, 'performance': performance})
    }), 200)
