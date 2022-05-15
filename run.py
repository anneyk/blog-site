from flask import Flask, render_template

#create a Flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
def index():
  return "<h1>Home Page</h1>"

@app.route('/user/<name>')
def user(name):
  return "<h1>Hello {}</h1>".format(name)