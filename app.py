from unicodedata import name
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return 'Welcome %s' %name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))


'''@app.route('/home', methods=['GET', 'POST'])
def home():
	links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
	return render_template('example.html', links=links)
    '''

if __name__ == '__main__':
	app.run(debug=True)