from flask import Flask, jsonify
import random
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)



#_____________1___________
@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"

#_____________2___________
car_list = ["Chevrolet", "Renault", "Ford", "Lada"]
@app.route("/cars")
def get_cars():
    return ", ".join(car_list)
#_____________3___________
cat_list = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
@app.route("/cats")
def get_cats():
    return f"{random.choice(cat_list)}"

#_____________4___________
@app.route("/get_time/now")
def get_time_now():
    current_time = datetime.now()
    return f"«Точное время {current_time}»"

#_____________5___________
@app.route("/get_time/future")
def get_time_future():
    current_time_after_hour = datetime.now() + timedelta(hours = 1)
    return f"«Точное время через час будет {current_time_after_hour}»"
#_____________6___________
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def load_words():
    with open(BOOK_FILE, encoding='utf-8') as book:
        text = book.read()
        # Используем регулярные выражения для получения списка слов без знаков препинания
        words = re.findall(r'\b\w+\b', text)
    return words


words_list = load_words()

@app.route('/get_random_word', methods=['GET'])
def get_random_word():
    random_word = random.choice(words_list)
    return  random_word

#_____________7___________
@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Страница открыта {counter.visits} раз(а)'

counter.visits = 0


if __name__ == '__main__':
    app.run(debug=True)