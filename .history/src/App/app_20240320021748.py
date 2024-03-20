from flask import Flask, request, render_template
import pickle
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

import pickle

# Cargar el modelo desde el archivo pickle
with open('modelo.pkl', 'rb') as f:
    model = pickle.load(f)

#model = pickle.load(open('C:/Users/Lucia/Desktop/bootcamp/DS_PT_09_2023/Data_Engineer/Docker/App/best_model.pkl', 'rb'))
#model = pickle.load(open('modelo.pkl', 'rb'))

print(model)
'''
#dic_target = {0:"NO SOBREVIVE ❌😥",
              1:"SOBREVIVE🤩"}

print(model)

#app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def home():
    return render_template('index.html')

@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('datos.html', name=name)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    Pclass_1 = float(data.get('Pclass1',1))
    Pclass_2 = float(data.get('Pclass2',1))
    Pclass_3 = float(data.get('Pclass3',1))
    is_male = int(data.get('is_male',1))
    Embarked_C=float(data.get('Embarked_C',1))
    Embarked_Q=float(data.get('EmbarkedQ',1))
    Embarked_S=float(data.get('Embarked_S',1))
    Age = float(data.get('Age'))
    Fare = float(data.get('Fare'))
    Acompaniantes = int(data.get('Acompaniantes'))
    prediction = model.predict([ [Pclass_1, Pclass_2,Pclass_3, is_male, Age,Embarked_C,Embarked_Q,Embarked_S, Fare, Acompaniantes]])

    prediction_message = dic_target.get(prediction[0], 'No se pudo determinar el resultado')
    return 'La predicción es {}'.format(prediction_message)
    
    #return 'La predicción es {}'.format(prediction)
    #return 'La predicción es {}'.(dic_target[model.predict([prediction])[0]])




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    '''