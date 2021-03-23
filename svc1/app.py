from flask import Flask,request
import requests
import json
app = Flask(__name__)

@app.route('/api/alive')
def hello_world():
    return { "msg" : "Server is running"}

@app.route('/api/addition',methods=['POST'])
def addition():
    request_data = request.get_json()
    data = json.dumps(request_data)
    print(data)
    response_sv2 = requests.post("http://localhost:8080/api/addition",json=data)
    return response_sv2.json()
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9090)