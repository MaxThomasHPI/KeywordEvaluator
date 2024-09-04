#import os

#from flask import Flask, request
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

#from services.users import user_management
#from database import models

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#print(app.config['SQLALCHEMY_DATABASE_URI'])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

"""
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! New!'


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user_management.add_user(data, db)

    return "Success!"

"""
from app_data import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
