from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

initial_food = (
    ("한식", "닭도리탕"), ("한식", "간장게장"), ("한식", "냉면"), ("한식", "설렁탕"), ("한식", "김치찌개"),
    ("한식", "불고기"), ("한식", "곱창"), ("한식", "삼겹살"), ("한식", "콩나물국밥"), ("한식", "보쌈"),

    ("중식", "짜장면"), ("중식", "짬뽕"), ("중식", "탕수육"), ("중식", "깐풍기"), ("중식", "울면"),
    ("중식", "유린기"), ("중식", "칠리새우"), ("중식", "마라탕"), ("중식", "마라샹궈"), ("중식", "꿔바로우"),

    ("일식", "스시"), ("일식", "우동"), ("일식", "돈가스"), ("일식", "소바"), ("일식", "야끼볶음우동"),
    ("일식", "오코노미야끼"), ("일식", "장어덮밥"), ("일식", "라멘"), ("일식", "타코야끼"), ("일식", "사케동"),

    ("양식", "스테이크"), ("양식", "피자"), ("양식", "까르보나라"), ("양식", "토마토스파게티"), ("양식", "햄버거"),
    ("양식", "도넛"), ("양식", "샐러드"), ("양식", "감바스"), ("양식", "리조또"), ("양식", "알리오올리오")
)


class Dish(db.Model):
    # DB 데이터 클래스, 초기 음식 삽입을 위해 init.py 내에서 따로 정의함.
    # models.py의 클래스를 여기에 import하면 ImportError(circular import) 발생함!!!
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    type = db.Column(db.String(4))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/msi/PycharmProjects/KAU_Computer_Network/website/' + DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from website.views import views
    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    return app


def create_database(app):  # db 파일이 없을 때 생성
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()

        for type, name in initial_food:
            new_food = Dish(name=name, type=type)
            with app.app_context():
                db.session.add(new_food)
                db.session.commit()
        print('>>> Create DB')
