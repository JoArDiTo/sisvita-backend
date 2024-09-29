from flask import Blueprint, request, jsonify, make_response
from .models import Question
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import questions_schema

questions = Blueprint('questions', __name__)

@questions.route('/add', methods=['POST'])
def addQuestion():    
    content = data().get('content')
    template_test_id = data().get('template_test_id')
    
    if not content or not template_test_id:
        return make_response(jsonify({'message': 'Content and Template Test id are required'}), 400)
    
    new_question = Question(content, template_test_id)
    db.session.add(new_question)
    db.session.commit()
    
    return make_response(jsonify({
        'message': 'Question registered successfully',
        'id': new_question.id
    }), 201)