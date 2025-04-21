from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Allow cross-origin requests
CORS(app)

# Load the model and vectorizer
model = joblib.load('spam.pkl')            # Load the trained model (spam.pkl)
vectorizer = joblib.load('text_vectorizer.pkl') # Load the vectorizer (vectorized.pkl)

# Define the root route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')  # Ensure your HTML file is named 'index.html'

# Define a route for predicting spam
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from POST request
    comment = data['comment']  # Extract the comment text
    
    # Transform the input text using the same vectorizer
    comment_vectorized = vectorizer.transform([comment])
    
    # Make the prediction
    prediction = model.predict(comment_vectorized)
    
    # Return the result
    result = 'spam' if prediction[0] == 1 else 'not spam'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
