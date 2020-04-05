from flask import Flask
from flask import jsonify

import functions


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify('API'), 200

@app.route('/servicio/v2/prediccion')
def prediction():
    response = functions.getData()
    return jsonify(response), 200    

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)

