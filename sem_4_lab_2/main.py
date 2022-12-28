from flask import Flask, request

app = Flask(__name__)

@app.route('/directory', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def directory():
   if request.method == 'POST':
      return 400
   elif request.method == 'GET':
      return 400
   elif request.method == 'PATCH':
      return 400
   else:
      return 400

@app.route('/binaryfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def binaryfile():
   if request.method == 'POST':
      return 400
   elif request.method == 'GET':
      return 400
   elif request.method == 'PATCH':
      return 400
   else:
      return 400

@app.route('/logtextfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def logtextfile():
   if request.method == 'POST':
      return 400
   elif request.method == 'GET':
      return 400
   elif request.method == 'PATCH':
      return 400
   else:
      return 400

@app.route('/bufferfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def bufferfile():
   if request.method == 'POST':
      return 400
   elif request.method == 'GET':
      return 400
   else:
      return 400

if __name__ = '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)