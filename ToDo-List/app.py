from flask import Flask, url_for, redirect, render_template
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.67.186.139:3306/tododb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "abcdefg"   # Always needs a secret Key for CRSF and WTForms

db = SQLAlchemy(app)

# Creates table in database 
class Todos(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default = False)

# Creates a form with a string input and submit field
class TodoForm(FlaskForm):
    task = StringField ("Task To Do: ")
    submit = SubmitField(" Add New Task")

# Shows all current todos (completed) - refers to index.html
@app.route("/")
def index():
    all_todos = Todos.query.all()
    return render_template("index.html", all_todos=all_todos)

# Adds a new todo to task and redirects to index and renders to add.html
@app.route("/add", methods=["GET", "POST"])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todos(task=form.task.data)  #task.data makes sure data in the box is read
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


# Completes todo linking with todo_id - must commit
@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return redirect(url_for("index"))
    
#url_for("complete", todo_id=1)

# Incomplete todo linking with todo_id - must commit 
@app.route("/incomplete/<int:todo_id>")
def incomplete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return redirect(url_for("index"))

# Deletes To Do then redirects to index - must delete and commit
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.delete(todo)
    db.session.commit()
    return redirect (url_for("index"))

# Updates To Do List
@app.route("/update/<int:todo_id", methods=["GET", "POST"])
def update(todo_id):
    form = TodoForm()
    todo_update = Todos.query.get(todo_id)
    if form.validate_on_submit():
        todo_update = Todos(task=form.task.data)  #task.data makes sure data in the box is read
        db.session.commit()
        return redirect(url_for("index"))
    elif request.method == "GET":
        form.task.data = todo_update.task
    return render_template("add.html", form=form)

# If they make a GET request

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')


## http://127.0.0.1:5000/ = local host