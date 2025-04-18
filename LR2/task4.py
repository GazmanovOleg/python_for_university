from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/hello-world/<name>')
def say_hello(name):
	days = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
	day = datetime.today().weekday()
	if day in [2,4,5]:
		ending = 'й'
	else:
		ending = 'го'
	return f'Привет, {name}. Хороше{ending} {days[day]}!'

if __name__ == '__main__':
	app.run()
	



