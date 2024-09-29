import os
from .. import db, create_app
from .models import Course, KeywordGen, KeywordMan, KeywordGenCourse, KeywordManCourse
import pandas as pd

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, "courses_data", "manuel_vs_generated_including_descriptions_fixed_en.csv")
    path = os.path.abspath(path)

    data = pd.read_csv(path, encoding='utf-8')

    for i, row in data.iterrows():

        title = row["title_en"]
        description = row["description_en"]

        course = Course(title=title, description=description)

        db.session.add(course)
        db.session.commit()

        man_keywords = list(set(row["manual_keywords"].split(';')))

        for k in man_keywords:
            existing_keyword = KeywordMan.query.filter_by(keyword=k).first()

            if not existing_keyword:
                db.session.add(KeywordMan(keyword=k))
                db.session.commit()

        gen_keywords = list(set(row["generated_keywords"].split(';')))

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
