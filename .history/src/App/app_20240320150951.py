from flask import Flask, request, render_template
import pickle
import os

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
    
   prediction = model.predict([Fecha])  # Realizar la predicción con tu modelo
    
    # Asumiendo que `prediction` es el resultado de tu modelo,
    # y deseas devolver este resultado como un mensaje
    prediction_message = str(prediction)

    return 'La predicción es {}'.format(prediction_message)
    