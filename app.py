import os

from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    score = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, dict):
        self.id = dict['id']
        self.name = dict['name']
        self.score = dict['score']

    def __repr__(self):
        return '<Student %r (%i)>' % (self.name, self.id)


@app.route("/")
def home():
    students = Student.query.all()
    return render_template("home.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        student = Student({
            'id': request.form.get('id'),
            'name': request.form.get('name'),
            'score': request.form.get('score')})
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")


@ app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == 'POST':
        student = Student.query.get(id)
        student.id = request.form.get('id')
        student.name = request.form.get('name')
        student.score = request.form.get('score')
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", student=Student.query.get(id))


@ app.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    if request.method == 'POST':
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('home'))

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
