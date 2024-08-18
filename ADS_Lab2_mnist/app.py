from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
app = Flask(__name__)

# Load the pre-trained MNIST model
model = load_model('mnist_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    image = np.array(data['image']).reshape(1, 28, 28, 1)  # Reshape to match model input
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    return jsonify({'digit': int(digit)})

if __name__ == "__main__":
    app.run(debug=True)
