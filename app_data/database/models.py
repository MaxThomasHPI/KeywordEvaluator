"""
Here the data models for the interaction with the database are stored.

"""
from .. import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    occupation = db.Column(db.String(100))

    courses = db.relationship('Course', backref='user', lazy=True)


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    user_choice = db.Column(db.String(10), nullable=True)
    start = db.Column(db.DateTime, nullable=True)
    end = db.Column(db.DateTime, nullable=True)

    keywords_gen = db.relationship('KeywordGen', secondary='keywords_gen_courses', backref='courses', lazy=True)
    keywords_man = db.relationship('KeywordMan', secondary='keywords_man_courses', backref='courses', lazy=True)


class KeywordGen(db.Model):
    __tablename__ = 'keywords_gen'

    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(255), unique=True)


class KeywordMan(db.Model):
    __tablename__ = 'keywords_man'

    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(255), unique=True)


class KeywordGenCourse(db.Model):
    __tablename__ = 'keywords_gen_courses'

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    keyword_id = db.Column(db.Integer, db.ForeignKey('keywords_gen.id'), primary_key=True)


class KeywordManCourse(db.Model):
    __tablename__ = 'keywords_man_courses'

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    keyword_id = db.Column(db.Integer, db.ForeignKey('keywords_man.id'), primary_key=True)
