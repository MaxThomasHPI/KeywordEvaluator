from app_data.database import models
from ... import db


def add_user(data):
    age_group = data.get("age_group")
    gender = data.get("gender")
    occupation = data.get("occupation")

    new_user = models.User(age_group=age_group, gender=gender, occupation=occupation)

    db.session.add(new_user)
    db.session.commit()
