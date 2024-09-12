import os
from .. import db, create_app
from .models import Course, KeywordGen, KeywordMan, KeywordGenCourse, KeywordManCourse

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    path = os.path.join(os.path.realpath(__file__), "../courses_data/manuel_vs_generated_including_descriptions_fixed.csv")

    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()

    lines = data.split('\n')[1:]

    for line in lines:
        line = line.split(',')

        title = line[4]
        description = line[7]

        course = Course(title=title, description=description)

        db.session.add(course)
        db.session.commit()

        man_keywords = list(set(line[5].split(';')))

        for k in man_keywords:
            existing_keyword = KeywordMan.query.filter_by(keyword=k).first()

            if not existing_keyword:
                db.session.add(KeywordMan(keyword=k))
                db.session.commit()

        gen_keywords = list(set(line[6].split(';')))
        for k in gen_keywords:
            existing_keyword = KeywordGen.query.filter_by(keyword=k).first()

            if not existing_keyword:
                db.session.add(KeywordGen(keyword=k))
                db.session.commit()

        for k in man_keywords:
            temp_keyword = KeywordMan.query.filter_by(keyword=k).first()

            db.session.add(KeywordManCourse(course_id=course.id, keyword_id=temp_keyword.id))
            db.session.commit()

        for k in gen_keywords:
            temp_keyword = KeywordGen.query.filter_by(keyword=k).first()

            db.session.add(KeywordGenCourse(course_id=course.id, keyword_id=temp_keyword.id))
            db.session.commit()
