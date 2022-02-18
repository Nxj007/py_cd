from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello There!</h1>'

@app.route('/')
def index():
	print url_for('give_greeting', name='Mark') 
# This will print '/greeting/Mark'

	
'''def give_greeting(name):
    return 'Hello, {0}!'.format(name)

app.add_url_rule('/greeting/<name>', 'give_greeting', give_greeting)

@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello, {0}!'.format(name)'''

if __name__ == '__main__':
	app.run(debug=True)