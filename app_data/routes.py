from flask import Blueprint, request
from app_data.services.users import user_management

main = Blueprint('main', __name__)


@main.route('/')
def initialize():
    return "Initialized!"


@main.route('/add_user', methods=["POST"])
def add_user():
    user_management.add_user(request.json)

    return "Success!"
