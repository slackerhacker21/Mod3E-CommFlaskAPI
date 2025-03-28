# routes/users.py
from flask import Blueprint, request, jsonify
from db import db
from models import User
from schemas import user_schema, users_schema

user_routes = Blueprint('users', __name__)

@user_routes.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], address=data['address'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@user_routes.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@user_routes.route('/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@user_routes.route('/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    data = request.get_json()
    user.name = data['name']
    user.address = data['address']
    user.email = data['email']
    db.session.commit()
    return user_schema.jsonify(user)

@user_routes.route('/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})
