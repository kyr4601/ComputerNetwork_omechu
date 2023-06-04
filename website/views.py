from flask import Blueprint, render_template, request
from website.models import Dish
from website.init import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        option = request.form.get('list')
        if option == 'Ko':
            type = "한식"
        elif option == 'Jp':
            type = "일식"
        elif option == 'Us':
            type = "양식"
        elif option == 'Cn':
            type = "중식"
        action = request.form.get('action')

        if action == '등록':
            new_food = Dish(name=name, type=type)
            db.session.add(new_food)
            db.session.commit()
        elif action == '삭제':
            dish_to_delete = Dish.query.filter_by(name=name, type=type).first()
            if dish_to_delete:
                db.session.delete(dish_to_delete)
                db.session.commit()

    return render_template('home.html')

