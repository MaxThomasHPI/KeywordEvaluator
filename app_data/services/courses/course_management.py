from sqlalchemy.sql import func, text
from datetime import datetime
from ...database import models
from ... import db
from ...helper_functions import helper


def pick_random_course():
    return models.Course.query.filter_by(user_id=None).order_by(func.random()).first()


def assign_course_to_user(user_id):
    course = pick_random_course()

    course.user_id = user_id
    course.start = datetime.now()

    db.session.commit()

    return course


def gather_course_information(course):
    course_id = course.id
    title = course.title
    description = course.description

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
        "genKeywords": gen_keywords,
        "manKeywords": man_keywords
    }


def select_course_for_user(user_id):
    course = assign_course_to_user(user_id)

    return gather_course_information(course)


def add_user_choice_to_course(course_id, choice):
    course = db.session.query(models.Course).filter(models.Course.id == course_id)

    course.user_choice = choice
    course.end = datetime.now()

    db.session.commit()
