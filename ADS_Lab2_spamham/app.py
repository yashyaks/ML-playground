import pandas as pd
from flask import Flask, request, render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
#cv = pickle.load(open('cv.pkl', 'rb'))
data = pd.read_table(r'C:/Users/Yash Thakar/PROGRAMMING/spam_ham/SMSSpamCollection.txt', sep='\t', names=["label", "message"])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    message = request.form.get('Message') # Assuming the input field name in your form is 'rate'
    cv = CountVectorizer(max_features=2500, binary=True)
    cv.fit_transform(data['message'])
    X = cv.transform([message])  # Use the CountVectorizer to transform the input

    prediction = model.predict(X)

    if prediction[0] == True:
        prediction_text = "The message is classified as spam."
    else:
        prediction_text = "The message is classified as ham (non-spam)."

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)