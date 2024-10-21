from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
from flask_cors import CORS
import mysql.connector as MYSQL
import json
import numpy as np
import os, uuid

app = Flask(__name__)
CORS(app)

@app.route("/Students", methods=["GET"])
def main():
    #city = request.args.get('Town')
    f = open('students.json')
    data = json.load(f)
    #filtered_data = [x for x in data if x['City'] == city]
    f.close()
    return data
    #return filtered_data, 200
    #return "Hello",200

@app.route("/Predict", methods=["GET"])
def predict():
    scores = request.args.get('Scores')
    y = [int(i) for i in scores.split(' ')]
    y = tuple(y)
    x = (1,2,3,4,5)
    m, b = np.polyfit(x, y, 1)
    predict = m * 6 + b
    if(predict > 100):
        predict = 100
    elif(predict < 0):
        predict = 0
    return str(predict), 200

if __name__ == "__main__":
    app.run()
