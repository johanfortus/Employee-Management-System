from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)
app.secret_key = "Secret Key"

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:newpassword@localhost/crud'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/crud'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# try:
#     conn = MySQLdb.connect(host="localhost", user="root", passwd="newpassword", db="crud")
#     print("Connected successfully")
#     conn.close()
# except MySQLdb.Error as e:
#     print(f"Error connecting to MySQL: {e}")

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="crud")
    print("Connected successfully")
    conn.close()
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")



class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route('/')
def homePage():
    all_data = Data.query.all()

    return render_template("home.html", employees = all_data)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        success_message = "Employee Inserted Successfully"
        flash(success_message)

        return redirect(url_for('homePage'))

        
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        message = "Employee Updated Successfully"
        flash(message)

        return redirect(url_for('homePage'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('homePage'))