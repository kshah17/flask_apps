from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///"
app.config['SECRET_KEY'] = "TEST"

db = SQLAlchemy(app)

# creates table in database
class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)

# creates online form
class RegisterForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

db.create_all()

# route to access this
@app.route('/', methods=["GET","POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        person = Register(name=form.name.data)
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')


## Codes to run tests: 

## Execute the test and include a coverage report by running:
# pytest --cov .

## We can test the coverage of just the app.py file by running:
# pytest --cov=app

## We can see which lines of code we haven't been able to test by running:
# pytest --cov=app --cov-report=term-missing

## We can also save the coverage report to a HTML file by running the following:
# pytest --cov . --cov-report html