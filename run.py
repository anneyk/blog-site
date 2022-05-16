from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "pixie"

#create a Form class
class NameForm(FlaskForm):
  name = StringField("What's your name", validators=[DataRequired()])
  submit = SubmitField("Submit")
  
#create a route decorator
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user/<name>')
def user(name):
  return render_template("user.html", name=name)

#create name page
@app.route('/name', methods=['GET','POST'])
def name():

  name = None
  form = NameForm()
  #validate Form
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
    flash("Form submitted successfully")
    
  return render_template("name.html", name=name, form=form)