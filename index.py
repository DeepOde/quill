from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/res', methods=['POST'])
def res():
    s = 'abcdefghijkl'
    l = list(s)
    req = request.get_json()
    print(req)
    res = jsonify(l[req]), 200

    return res