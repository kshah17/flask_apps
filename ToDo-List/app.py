from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.225.186.188/tododb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Todos(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default = False)

@app.route("/")
def index():
    all_todos = Todos.query.all()
    todos_String = " "
    for todo in all_todos:
        todos_String += "<br>" + str(todo.id)+ " " + todo.task 
    return "This Is a TODO List!"

@app.route('/add')
def add():
    new_todo = Todos(name="New ToDo")
    db.session.add(new_todo)
    db.session.commit()
    return new_todo.task

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return "Completed To Do"

@app.route("/incomplete/<int:todo_id>")
def incomplete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return "Inomplete To Do"

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.delete(todo)
    db.session.commit()
    return "Deleted To Do"


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')


## http://127.0.0.1:5000/ = local host