from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy

main = Blueprint('main', __name__)
db = SQLAlchemy(main)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(25), nullable=False)
    type = db.Column(db.String(2), nullable=False)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/test')
def test():
    return render_template('test.html')


@main.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    passord = request.form["password"]
    return render_template("register.html", username=username)
