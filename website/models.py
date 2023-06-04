from website.init import db  # from website import db


class Dish(db.Model): # DB 데이터 클래스
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    type = db.Column(db.String(4))