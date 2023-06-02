from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db 파일 경로. website 폴더 안에 생성해주세요' + DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from website.views import views
    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app


def create_database(app): # db 파일이 없을 때 db 파일 생성
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('>>> Create DB')
