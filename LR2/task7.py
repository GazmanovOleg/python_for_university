import datetime
from flask import Flask
app = Flask (__name__)
storage = {}

@app.route("/add/<date>/<int:number>")
def add (date: str, number: int):
    year = int (date[:4])
    month = int (date[4:6])
    day = int (date[6:8])
    if check_date (year, month, day):
        storage.setdefault(year, (}).setdefault(month, 0)
        storage[year][month] += number
    else:
        return 'Введенная дата некорректна, исправьте!!


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    try:
        return 
    except KeyError:
        return f'У меня пока нет данных по {уеаг} году и {month} месяцу. '
