from flask import Blueprint, request, jsonify
from ..Controllers import create_user, get_user_by_id, update_user, remove_user, login_user, get_all_users

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/create_user', methods=['POST'])
def create():
    data = request.get_json()
    res, status = create_user(data)
    return res, status

@user_bp.route('/<int:user_id>', methods=['GET'])
def get(user_id):
    res, status = get_user_by_id(user_id)
    return res, status

@user_bp.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    res, status = update_user(data)
    return res, status

@user_bp.route('/remove/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    res, status = remove_user(user_id)
    return res, status

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    res, status = login_user(data.get("email"), data.get("password"))
    return res, status

@user_bp.route("/all", methods=['GET'])
def all():
    res, status = get_all_users()
    return res, status