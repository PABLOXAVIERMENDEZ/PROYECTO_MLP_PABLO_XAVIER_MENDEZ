from flask import Flask, request, render_template
import pickle
import os



os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('modelo.pkl', 'rb'))

# Cargar el modelo desde el archivo pickle
#with open('modelo.pkl', 'rb') as f:
    #model = pickle.load(f)



#dic_target = {0:"NO SOBREVIVE ❌😥",
            #  1:"SOBREVIVE🤩"}
              

print(model)

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
    
    prediction = model.predict([ [Fecha]])

    prediction_message = data.get(prediction[0], 'No se pudo determinar el resultado')
    return 'La predicción es {}'.format(prediction_message)
    '''
    return 'La predicción es {}'.format(prediction)
    return 'La predicción es {}'.(dic_target[model.predict([prediction])[0]])
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    