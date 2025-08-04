import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Download NLTK dependencies if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load large dataset
df = pd.read_csv('chatbot_dataset_large.csv')

# Preprocess function
def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords]
    return " ".join(tokens)

# Apply preprocessing
df['processed_question'] = df['question'].apply(preprocess_text)

# Vectorize the text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['processed_question'])
y = df['intent']

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X, y)

# Save the model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer trained and saved successfully!")

