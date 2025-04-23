from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd


app = Flask(__name__)

CORS(app)


model = joblib.load('spam.pkl')         
vectorizer = joblib.load('text_vectorizer.pkl') 


@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  
    comment = data['comment']  

    comment_vectorized = vectorizer.transform([comment])
    
   
    prediction = model.predict(comment_vectorized)
    
  
    result = 'spam' if prediction[0] == 1 else 'not spam'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
