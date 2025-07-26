## Put and Delete - HTTP VERBS
## Working with API's -- json
from flask import Flask,jsonify,request

app = Flask(__name__)

##Initial Data in To Do List
items = [
    {"id1":1,"name":"Item 1","description":"This is item 1"}
    {"id1":2,"name":"Item 2","description":"This is item 2"}
]

@app.route('/')
def Home():
    return "Welcome to the Sample To Do List App"

## Retrievel of all items

@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

## get : Retreve a specific item by id

@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"==item_id]),None)
    if item is None:
        return jsonify({"error":"Item not find"})
    return jsonify(item)

## post : create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not find"})
    new_item = {
        "id":items[-1]["id"]+1 if items else 1
    }













if __name__=="__main__":
    app.run(debug=True)