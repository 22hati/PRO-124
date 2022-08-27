from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name':'John',
        'contact':"244-556-1111",
        'done':False
    },
    {
        'id': 2,
        'name':'Sara',
        'contact':"254-667-9992",
        'done':False
    }
]

@app.route('/get-data')

def get_task():
    return jsonify({
        "data":tasks
    })

@app.route('/add-data',methods = ['POST'])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        }, 400)

    task = {
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

if (__name__ == "__main__"):
    app.run()