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

N_TRAIN_ELEMENTS = 2000

@app.route('/')
def index():
    return jsonify('API'), 200

@app.route('/servicio/v1/prediccion/<h>')
def prediction(h):
    # Convert dtype: object to dtype: float
    df["humidity"] = pd.to_numeric(df["humidity"], errors='coerce')
    df["temperature"] = pd.to_numeric(df["temperature"], errors='coerce')
    prediction_hum = functions.prediction(df["humidity"], int(h), N_TRAIN_ELEMENTS)
    prediction_temp = functions.prediction(df["temperature"], int(h), N_TRAIN_ELEMENTS)

    response = []
    for i in range(int(h)):
        n = i % 24
        hour = "%02d:00" % n
        response.append({"hour": hour, "temp": prediction_temp[i], "hum": prediction_hum[i]})

    return jsonify(response), 200    


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)