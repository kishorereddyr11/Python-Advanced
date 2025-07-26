## How to integrate html File with Flask
from flask import Flask,render_template

## It create an instace of the flask class which will be your wgsi for application

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Wellcome To Flask Home Page....</h1>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return "<h1>Wellcome To Flask About Page....</h1>"


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 