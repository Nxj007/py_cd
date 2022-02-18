from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def index():
	return '<h1>Hello Admin Hello Admin </h1>'

@app.route('/admin1')
def index1():
	return '<h1> Hello Admin11 </h1>'

@app.route('/guest/<guest>')
def h_guest(guest):
	return '<h1>Hello %s is There! </h1>' %guest

@app.route('/user/<user11>')
def user(user11):
	if user11 == 'admin':
		return redirect(url_for('index'))
	#elif:
		#return redirect(url_for('index1'))
	else:
		return redirect(url_for('h_guest',guest=user11))
		#'<h1>0477</h1>' 


'''@app.route('/<int:a>')
def index(a):
	return '<h1>Hello %d There! </h1>'%a

@app.route('/ff/<float:b>')
def index2(b):
	return '<h1>Hello %f There! </h1>'%b
	'''

'''@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)
'''
if __name__ == '__main__':
	app.run(debug=True)