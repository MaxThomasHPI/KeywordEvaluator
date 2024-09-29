from sqlalchemy.sql import func, text
from datetime import datetime
from ...database import models
from ... import db
from ...helper_functions import helper


def pick_random_course():
    return models.Course.query.filter_by(user_id=None).order_by(func.random()).first()


def assign_course_to_user(user_id):

    if check_number_of_courses_for_user(user_id) < 10:
        course = pick_random_course()

        course.user_id = user_id
        course.start_time = datetime.now()

        db.session.commit()

        return course
    return None


def check_number_of_courses_for_user(user_id):
    query = text("SELECT COUNT(id) FROM courses WHERE user_id = :user_id")
    results = db.session.execute(query, {"user_id": user_id})
    return results.fetchone()[0]


def gather_course_information(course):
    course_id = course.id
    title = course.title
    description = course.description

    if description == 'NaN':
        description = None

    statement = text("SELECT keyword FROM keywords_gen WHERE id IN "  # sql statement needs to wraped into a text
                     "(SELECT keyword_id FROM keywords_gen_courses WHERE course_id = :course_id);")
    result = db.session.execute(statement, {'course_id': course_id})
    gen_keywords = helper.convert_list_of_single_tuples_to_list(result.fetchall())

    statement = text("SELECT keyword FROM keywords_man WHERE id IN "  # sql statement needs to wraped into a text
                     "(SELECT keyword_id FROM keywords_man_courses WHERE course_id = :course_id);")
    result = db.session.execute(statement, {'course_id': course_id})
    man_keywords = helper.convert_list_of_single_tuples_to_list(result.fetchall())

    return {
        "courseID": course_id,
        "title": title,
        "description": description,
        "gen": gen_keywords,
        "man": man_keywords
    }


def select_course_for_user(user_id):
    course = assign_course_to_user(user_id)

    if course:
        return gather_course_information(course)
    return None


def add_user_choice_to_course(course_id, choice):
    course = db.session.query(models.Course).filter(models.Course.id == course_id).first()

    course.user_choice = choice
    course.end_time = datetime.now()

    db.session.commit()
