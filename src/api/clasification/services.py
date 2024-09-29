from flask import Blueprint, request, jsonify, make_response
from .models import Clasification
from src.common.utils.db import db
from src.common.utils.data import data

clasifications = Blueprint('clasifications', __name__)

@clasifications.route('/add', methods=['POST'])
def addClasification():
    min_score = data().get('min_score')
    max_score = data().get('max_score')
    interpretation = data().get('interpretation')
    template_test_id = data().get('template_test_id')
    
    if min_score is None or max_score is None or not interpretation or not template_test_id:
        return make_response(jsonify({'message': 'All fields are required'}), 400)
    
    new_clasification = Clasification(min_score, max_score, interpretation, template_test_id)
    db.session.add(new_clasification)
    db.session.commit()
    
    return make_response(jsonify({
        'message': 'Clasification registered successfully',
        'id': new_clasification.id
    }), 201)