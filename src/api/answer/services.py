from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required
from .models import Answer
from src.common.utils.db import db
from src.common.utils.data import data

answers = Blueprint('answers', __name__)

@answers.route('/add/<string:test_id>', methods=['POST'])
@jwt_required()
def addAnswersBy(test_id):    
    performace = data().get('performance')
    
    if not performace:
        return make_response(jsonify({'message': 'performance field is required'}), 400)
    
    for p in performace:
        question_id = p.get('question_id')
        alternative_id = p.get('alternative_id')
        
        if not question_id or not alternative_id:
            return make_response(jsonify({'message': 'All fields are required'}), 400)
    
        new_answer = Answer(test_id, question_id, alternative_id)
        db.session.add(new_answer)
        
    db.session.commit()
    
    return make_response(jsonify({
        'message': f'{len(performace)} answers registered successfully in test {test_id}',
    }), 201)
