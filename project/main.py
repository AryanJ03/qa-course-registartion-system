from flask import Blueprint, render_template

main = Blueprint('main', __name__)

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
