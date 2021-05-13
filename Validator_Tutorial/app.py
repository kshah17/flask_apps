# 1.set up flask object

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY'

# 2. Create Validator 

class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = 'Please choose another username'
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

# Here we set up the class (L14) to have the banned and message attributes. banned must be passed through at declaration.
# If no message chosen, then this default message(L17)is returned.


# 3. Create simpleform with username = stringfield

class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        UserCheck(message="custom rejection message",banned = ['root','admin','sys']),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')


# 4.This is the app route, the function that defines the behaviour of our app. When the form is submitted,
# it will render the home.html page with the username variable set to the form submission. Otherwise, it will render it as an empty string.

@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form = form, username=username)
    else:
        return render_template('home.html', form = form, username="")


# 5. Allows to be run from commandline (locally)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')