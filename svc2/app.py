from flask import Flask,request
import json
app = Flask(__name__)

@app.route('/api/addition')
def hello_world():
    return 'Hello, World!'

@app.route('/api/addition',methods=['POST'])
def addition():
    print(request)
    request_data = json.loads(request.get_json())
    summation = request_data['a']+ request_data['b']
    return { "result" : summation}
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)