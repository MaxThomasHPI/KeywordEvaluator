from app_data.services.courses import course_management
from app_data import create_app


app = create_app()

with app.app_context():
    print(course_management.gather_course_information(course_management.pick_random_course()))
