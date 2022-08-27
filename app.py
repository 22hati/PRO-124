from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':'Book',
        'description':'The book is good.',
        'done': False
    },
    {
        'id':2,
        'title':'Science',
        'description':'Very intiguing',
        'done': False
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
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

if (__name__ == "__main__"):
    app.run()