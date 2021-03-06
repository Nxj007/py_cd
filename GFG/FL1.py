from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/users'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

if __name__ == '__main__':
	app.run()
