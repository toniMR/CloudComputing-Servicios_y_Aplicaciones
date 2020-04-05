from flask import Flask
from flask import jsonify
from pymongo import MongoClient
import pandas as pd
import functions

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client["cc-db"]
collection = db['weather']
df = pd.DataFrame(collection.find({}))

@app.route('/')
def index():
    return jsonify('API'), 200

@app.route('/prediction/predict/<predict>/hours/<h>/elements/<elements>')
def prediccion24(predict, h, elements):
    # Convert dtype: object to dtype: float
    df[predict] = pd.to_numeric(df[predict], errors='coerce')
    prediction = functions.prediction(df[predict], int(h), int(elements))
    response = {
        'predict': predict,
        'hours': int(h),
        'elements': int(elements),
        'prediction': prediction.tolist()
    }
    return jsonify(response), 200
    


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)