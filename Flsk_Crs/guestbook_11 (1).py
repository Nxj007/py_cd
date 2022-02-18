from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:a>')
def index(a):
	return '<h1>Hello %d There! </h1>'%a

@app.route('/ff/<float:b>')
def index2(b):
	return '<h1>Hello %f There! </h1>'%b

@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)

if __name__ == '__main__':
	app.run(debug=True)