from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
conn = Flask(__name__)
# MySQL configurations
conn.config['MYSQL_DATABASE_USER'] = 'root'
conn.config['MYSQL_DATABASE_PASSWORD'] = ''
conn.config['MYSQL_DATABASE_DB'] = 'test'
conn.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(conn)