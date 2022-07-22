from flask import Flask,jsonify

todos = { "label": "My second task", "done": False }

app = Flask(__name__)

@app.route('/blabla',methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos',methods=['GET'])
def hello():
    return jsonify(todos), 400

if __name__=='__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)