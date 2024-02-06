from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'viswa@3366'
app.config['MYSQL_DB'] = 'viswa'

mysql = MySQL(app)

@app.route('/register', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
         details = request.form
         username = details['uname']
         email = details['email']
         password = details['pass']
         cur = mysql.connection.cursor()
         cur.execute("INSERT INTO users(username, email, password) VALUES(%s,%s,%s)", (username, email, password))
         mysql.connection.commit()
         cur.close()
         return 'success'
    return render_template('index.html', message='hello')


@app.route('/list', methods=['GET', 'POST'])
def listname():
    if request.method == "GET":
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM MyUsers")
         data = cur.fetchall()
    return render_template('listname.html', value=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')