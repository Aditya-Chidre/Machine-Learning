from flask import Flask, jsonify, request

app = Flask('__name__')

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to To Do List App"

# Getting all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# Getting item by specific id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"Error":"Item not found"})
    return jsonify(item)

# Inserting new item
@app.route('/items',methods=['POST'])
def insert():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error":"Insert details"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(items)

# Updating the details
@app.route('/items/<int:item_id>',methods=['PUT'])
def update(item_id):
    item = next((item for item in items if item["id"]==item_id), None)
    if item is None:
        return jsonify({"Error": "Item mot found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)

# Delete the item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete(item_id):
    global items
    items= [item for item in items if item["id"] != item_id]
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
    