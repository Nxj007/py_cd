from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'users'
 
mysql = MySQL(app)

#Creating a connection cursor
cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
 
#Executing SQL Statements
cursor.execute(''' CREATE TABLE info_table(field1, field2...) ''')
cursor.execute(''' INSERT INTO info_table VALUES(v1,v2...) ''')
cursor.execute(''' DELETE FROM info_table WHERE condition ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()
 
#Closing the cursor
cursor.close()

