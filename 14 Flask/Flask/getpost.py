## How to integrate html File with Flask

## It create an instace of the flask class which will be your wgsi for application

## WSGI Application
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome To Flask Home Page</h1>"

@app.route('/form', methods=['GET', 'POST'])
def show_form():
    if request.method == 'POST':
        name = request.form.get('name')  # Safer way with default value
        return f"Hello {name}!"
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    name = request.form.get('name')
    return f"Hello {name} from submit page!"

if __name__ == '__main__':
    app.run(debug=True)