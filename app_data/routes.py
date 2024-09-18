from flask import Blueprint, request, render_template
from app_data.services.users import user_management
from app_data.services.web_site_services import website_builder

main = Blueprint('main', __name__)


@main.route('/')
def initialize():
    #return "Initialized!"
    return render_template("index.html")


@main.route('/get_introduction_text')
def get_introduction_text():
    return website_builder.get_introduction_text()


@main.route('/add_user', methods=["POST"])
def add_user():
    user_management.add_user(request.json)

    return "Success!"
