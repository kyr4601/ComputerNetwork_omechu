from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

initial_food = (
    ("ko", "닭도리탕"), ("ko", "간장게장"), ("ko", "냉면"), ("ko", "설렁탕"), ("ko", "김치찌개"),
    ("ko", "불고기"), ("ko", "곱창"), ("ko", "삼겹살"), ("ko", "콩나물국밥"), ("ko", "보쌈"),

    ("ch", "짜장면"), ("ch", "짬뽕"), ("ch", "탕수육"), ("ch", "깐풍기"), ("ch", "울면"),
    ("ch", "유린기"), ("ch", "칠리새우"), ("ch", "마라탕"), ("ch", "마라샹궈"), ("ch", "꿔바로우"),

    ("jp", "스시"), ("jp", "우동"), ("jp", "돈가스"), ("jp", "소바"), ("jp", "야끼볶음우동"),
    ("jp", "오코노미야끼"), ("jp", "장어덮밥"), ("jp", "라멘"), ("jp", "타코야끼"), ("jp", "사케동"),

    ("us", "스테이크"), ("us", "피자"), ("us", "까르보나라"), ("us", "토마토스파게티"), ("us", "햄버거"),
    ("us", "도넛"), ("us", "샐러드"), ("us", "감바스"), ("us", "리조또"), ("us", "알리오올리오")
)


class Dish(db.Model):
    # DB 데이터 클래스, 초기 음식 삽입을 위해 init.py 내에서 따로 정의함.
    # models.py의 클래스를 여기에 import하면 ImportError(circular import) 발생함!!!
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=True)
    type = db.Column(db.String(20))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////ComputerNetwork_omechu-OMECHU_modified/ComputerNetwork_omechu-OMECHU_modified/website/' + DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    from views import views
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
