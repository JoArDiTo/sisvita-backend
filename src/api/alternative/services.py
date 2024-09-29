from flask import Blueprint, request, jsonify, make_response
from .models import Alternative
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import alternatives_schema

alternatives = Blueprint('alternatives', __name__)

@alternatives.route('/add', methods=['POST'])
def addAlternative():    
    content = data().get('content')
    value = data().get('value')
    template_test_id = data().get('template_test_id')
    
    if not content or value is None or not template_test_id:
        return make_response(jsonify({'message': 'All fields are required'}), 400)
    
    new_alternative = Alternative(content, value, template_test_id)
    db.session.add(new_alternative)
    db.session.commit()
    
    return make_response(jsonify({
        'message': 'Alternative registered successfully',
        'id': new_alternative.id
    }), 201)