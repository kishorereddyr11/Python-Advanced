from flask import Flask

## It create an instace of the flask class which will be your wgsi for application

## WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Wellcome To Flask Home Page...."

@app.route("/index")
def index():
    return "Wellcome To Flask Index Page...."

@app.route("/about")
def about():
    return "Wellcome To Flask About Page...."


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 