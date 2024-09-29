from flask import Blueprint, jsonify, make_response
from .models import User
from src.common.utils.db import db
from src.common.utils.data import data
from .schema import user_schema
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies
)

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register():
    document_type = data().get('document_type')
    document_number = data().get('document_number')
    first_name = data().get('first_name')
    paternal_surname = data().get('paternal_surname')
    maternal_surname = data().get('maternal_surname')
    phone_number = data().get('phone_number')
    email = data().get('email')
    password = data().get('password')
    
    if not document_type or not document_number or not first_name or not paternal_surname or not maternal_surname or not phone_number or not email or not password:
        return make_response(jsonify({'message': 'All fields are required'}), 400)
    
    user = User.query.filter_by(document_number=document_number).first()
    if user:
        return make_response(jsonify({'message': 'Document number already registered'}), 400)
    
    user = User.query.filter_by(email=email).first()
    if user:
        return make_response(jsonify({'message': 'Email already registered'}), 400)
    
    new_user = User(document_type, document_number, first_name, paternal_surname, maternal_surname, phone_number, email, password)
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({
        'message': 'User registered successfully',
        'id': new_user.id
    }), 201)

@users.route('/login', methods=['POST'])
def login():
    email = data().get('email')
    password = data().get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return make_response(jsonify({'message': 'Invalid email or password'}), 401)

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    
    response = make_response(jsonify({
        'message': 'Login successful',
        #'access_token': access_token,
        #'refresh_token': refresh_token,
    }), 200)
    
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response

@users.route('/getProfile', methods=['GET'])
@jwt_required()
def getProfile():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    if not user:
        return make_response(jsonify({'message': 'User not found'}), 404)
    profile = user_schema.dump(user)
    return make_response(jsonify({
        'message': 'Profile retrieved successfully',
        'profile': profile
    }), 200)
    
@users.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = make_response(jsonify({'message': 'Logout successful'}), 200)
    unset_jwt_cookies(response)
    return response