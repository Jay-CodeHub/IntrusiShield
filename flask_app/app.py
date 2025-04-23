from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from chatbot import get_response

app = Flask(__name__)

# Load your models
model_vgg16 = load_model('models/VGG16.keras')
model_vgg19 = load_model('models/VGG19.keras')
model_xception = load_model('models/xception.keras')
model_resnet = load_model('models/resnet.keras')
model_inception = load_model('models/inception.keras')
model_inceptionresnet = load_model('models/inceptionresnet.keras')

# Preprocess the input data as per your model requirement
def preprocess_input(data):
    return np.array(data).reshape(1, -1)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form.getlist('data')
        model_choice = request.form['model']
        
        data = list(map(float, data))
        
        processed_data = preprocess_input(data)
        
        if model_choice == 'vgg16':
            model = model_vgg16
        elif model_choice == 'vgg19':
            model = model_vgg19
        elif model_choice == 'xception':
            model = model_xception
        elif model_choice == 'resnet':
            model = model_resnet
        elif model_choice == 'inception':
            model = model_inception
        elif model_choice == 'inceptionresnet':
            model = model_inceptionresnet
        
        prediction = model.predict(processed_data)
        result = 'Attack' if prediction[0][0] > 0.5 else 'Normal'
        
        return render_template('result.html', result=result)

@app.route('/recovery')
def recovery():
    return render_template('recovery.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
