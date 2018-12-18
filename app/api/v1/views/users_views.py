from flask import Flask, Blueprint, request, jsonify, make_response

from ..models import user_models

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

user = user_models.User_Accounts()


@auth.route('/signup', methods=['POST'])
def signup_user():
    ''' endpoint for creating user account '''

    user_data = request.get_json()
    if not user_data:
        return jsonify({"message": "Data set cannot be empty"})
    email = user_data.get('email').strip()
    username = user_data.get('username').strip()
    password = user_data.get('password').strip()

    res = jsonify(user.register_user(email, username, password))
    return res


@auth.route('/user/<username>', methods=['GET'])
def get_theUser(username):
    res = make_response(jsonify(user.get_user_data(username)))
    res_data = res.json()
    return res_data["username"]


@auth.route('/user/<username>/edit', methods=['PUT'])
def edit_username(username):
    username = user.get_user_data(username)
    new_username = request.get_json()["username"]
    username[0]["username"] = new_username
    return jsonify(username, {
        "message" : "username updated successfully"
    })

@auth.route('/user/<username>/delete', methods=['DELETE'])
def delete_username(username):
    pass
