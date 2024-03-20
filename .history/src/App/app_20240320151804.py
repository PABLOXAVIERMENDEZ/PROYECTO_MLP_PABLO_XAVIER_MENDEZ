from flask import Flask, request
import pickle
import numpy as np

# Cargar el modelo desde el archivo pickle
model = pickle.load(open('modelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    Fecha = data.get('Ingresar fecha')
    
    # Reformatear la entrada para que tenga el formato correcto (matriz 2D)
    fecha_2d = np.array([Fecha]).reshape(1, -1)
    
    # Realizar la predicción con tu modelo
    prediction = model.predict(fecha_2d)
    
    # Convertir la predicción a un mensaje legible
    prediction_message = str(prediction)

    return 'La predicción es {}'.format(prediction_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    