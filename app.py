from flask import Flask, request, render_template, jsonify
import json
import random

app = Flask(__name__)
# app.config("DEBUG") = True

@app.route('/', methods=["GET"])
def home():
    with open('./questions.json') as json_file:
        data = json.load(json_file)
        question = random.choice(data)
        print(question['number'])
        print(question['question'])
        q = question['question']
        t = question['type']
        return render_template('index.html', question=q, qtype=t)



