from flask import Blueprint, render_template, request, json
from init import db, Dish
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

views = Blueprint('views', __name__)
engine = create_engine('sqlite:///c:/Users/Kim YR/OneDrive/바탕 화면/0608/ComputerNetwork_omechu-OMECHU_modified/ComputerNetwork_omechu-OMECHU_modified/website/database.db')
Session = sessionmaker(bind=engine)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        option = request.form.get('list')
        if option == 'Ko':
            type = "ko"
        elif option == 'Jp':
            type = "jp"
        elif option == 'Us':
            type = "us"
        else:
            type = "ch"
        action = request.form.get('action')

        if action == '등록':
            new_food = Dish(name=name, type=type)
            db.session.add(new_food)
            db.session.commit()
        else:
            dish_to_delete = Dish.query.filter_by(name=name, type=type).first()
            if dish_to_delete:
                db.session.delete(dish_to_delete)
                db.session.commit()
    return render_template('home.html')

@views.route('/ko' , methods = ['GET'])
def komenu():
    session = Session()
    
    sql_expression = text('SELECT name FROM Dish WHERE type = :type ORDER BY RANDOM()')
    result = session.execute(sql_expression, {"type": "ko"})
    random_komenu = result.fetchone()
   
    komenu_keys = result.keys()
    komenu_dict = dict(zip(komenu_keys,random_komenu))
    ko_json_data = json.dumps(komenu_dict, ensure_ascii=False)
    
    
    return ko_json_data

@views.route('/jp' , methods = ['GET'])
def jpmenu():
    session = Session()
    
    sql_expression1 = text('SELECT name FROM Dish WHERE type = :type ORDER BY RANDOM()')
    result = session.execute(sql_expression1, {"type": "jp"})
    random_jpmenu = result.fetchone()
    jpmenu_keys = result.keys()
    jpmenu_dict = dict(zip(jpmenu_keys,random_jpmenu))
    jp_json_data = json.dumps(jpmenu_dict, ensure_ascii=False)   
    
    return jp_json_data
  
@views.route('/us' , methods = ['GET'])
def usmenu():
    session = Session()
    
    sql_expression = text('SELECT name FROM Dish WHERE type =:type ORDER BY RANDOM()')
    result = session.execute(sql_expression, {"type": "us"})
    random_usmenu = result.fetchone()
    usmenu_keys = result.keys()
    usmenu_dict = dict(zip(usmenu_keys,random_usmenu))
    us_json_data = json.dumps(usmenu_dict, ensure_ascii=False)   
    
    return us_json_data

@views.route('/ch' , methods = ['GET'])
def chmenu():
    session = Session()
    
    sql_expression = text('SELECT name FROM Dish WHERE type =:type ORDER BY RANDOM()')
    result = session.execute(sql_expression, {"type": "ch"})
    random_chmenu = result.fetchone()
    chmenu_keys = result.keys()
    chmenu_dict = dict(zip(chmenu_keys,random_chmenu))
    ch_json_data = json.dumps(chmenu_dict, ensure_ascii=False)   
    
    return ch_json_data

@views.route('/dummy', methods=['GET', 'POST'])
def dummy():
    return render_template('dummy.html')