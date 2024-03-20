from flask import Flask, request, render_template
import pickle
import os
import numpy as np
from datetime import datetime

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('modelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('datos.html', name=name)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    Fecha = data.get('Ingresar fecha')
    
    fecha_datetime = datetime.strptime(Fecha, '%Y-%m-%d')

     # Convertir la fecha en una matriz 2D
    fecha_numerica = np.array([fecha_datetime]).reshape(1, -1)
    
    
    # Realizar la predicción con tu modelo
    prediction = model.predict([fecha_numerica])
    # Convertir la predicción a un mensaje legible
    prediction_message = str(prediction)

    return 'La predicción es {}'.format(prediction_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    