from flask import Blueprint, request, render_template, jsonify
from app_data.services.users import user_management
from app_data.services.web_site_services import website_builder
from app_data.services.courses import course_management

main = Blueprint('main', __name__)


@main.route('/')
def initialize():
    return render_template("index.html")


@main.route('/get_introduction_text')
def get_introduction_text():
    return website_builder.get_introduction_text()


@main.route('/add_user', methods=["POST"])
def add_user():
    user_id = user_management.add_user(request.json)
    response = jsonify({"Status": "User_ID cookie has been set!"})
    response.set_cookie("user_id", str(user_id))
    return response


@main.route('/get_next_course')
def get_next_course():
    user_id = request.cookies.get('user_id')
    return jsonify(course_management.select_course_for_user(user_id))


@main.route('/set_user_choice', methods=["POST"])
def set_user_choice():
    course_id = request.json.get("course_id")
    choice = request.json.get("user_choice")
    course_management.add_user_choice_to_course(course_id, choice)
    return "Success!"
