from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user/<name>')
def user(name):
  return render_template("user.html", username=name)