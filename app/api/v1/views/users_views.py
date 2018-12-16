from flask import Flask, Blueprint, request, jsonify

from ..models import user_models

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

user = user_models.User_Accounts()

@auth.route('/signup', methods = ['POST'])
def signup_user():
    ''' endpoint for creating user account '''
    
    user_data = request.get_json()
    if not user_data:
        return jsonify({"message":"Data set cannot be empty"})
    email = user_data.get('email').strip()
    username = user_data.get('username')
    password = user_data.get('password')

    res = jsonify(user.register_user(email, username, password))
    return res