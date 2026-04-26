from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def home():
    return jsonify({"message": "API working"})