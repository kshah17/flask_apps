#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#@app.route('/home')
#def home():
#    return 'This is the home page'

#@app.route('/about')
#def about():
#    return 'This is the about page'

#if __name__ == "__main__":
#    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.90.233/test_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    

if __name__ == "__main__":
    app.run(debug=True)