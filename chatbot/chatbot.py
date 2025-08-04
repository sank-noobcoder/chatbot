from flask import Flask, render_template, request, jsonify
import nltk
import pickle
import pandas as pd

# Load the model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the large dataset for response mapping
df = pd.read_csv('chatbot_dataset_large.csv')

# Preprocess function
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords]
    return " ".join(tokens)

# Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    processed_input = preprocess_text(user_input)
    features = vectorizer.transform([processed_input])
    intent = model.predict(features)[0]
    
    # Get response for the predicted intent
    response = df[df['intent'] == intent].sample(n=1)['answer'].values[0]

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
