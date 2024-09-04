from sqlalchemy.sql import func
from datetime import datetime
from ...database import models
from ... import db


def pick_random_course():
    return db.session.query(models.Course).filter(models.Course.user_id is None).order(func.random()).first()


def assign_course_to_user(user_id):
    course = pick_random_course()

    course.user_id = user_id
    course.start = datetime.now()

    db.session.commit()


def add_user_choice_to_course(course_id, choice):
    course = db.session.query(models.Course).filter(models.Course.id == course_id)

    course.user_choice = choice
    course.end = datetime.now()

    db.session.commit()
