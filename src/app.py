from flask import Flask,jsonify,request
import json

todos = [ { "label": "My first task", "done": False }, ]
some_data = [ { "label": "My secund task", "done": False } ]

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text, 400
@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data)
    request_body = jsonify(request.data)
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)