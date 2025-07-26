## Building Url Dynamically
## Variable Rule
## Jinja 2 Templet Engine
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is Home Page</h1>"


@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form.get('name')
        return f"{name} Wellcome!"
    return render_template('form.html')

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>50:
        res = "Pass"
    else:
        res = "Fail"
    return render_template("result.html",result=res)

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>50:
        res = "Pass"
    else:
        res = "Fail"
    
    exp = {"score":score,"res":res}
    return render_template("result1.html",results=exp)

if __name__=='__main__':
    app.run(debug=True)