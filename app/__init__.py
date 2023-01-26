from flask import Flask, jsonify, request
from flask_cors import CORS
from .faker import faker_response

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    args = request.get_json()
    question = args["question"]

    answers = faker_response(question)
    return jsonify({"answer": answers})
