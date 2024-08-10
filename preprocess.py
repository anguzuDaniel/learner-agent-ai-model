import json
import nltk
from nltk.stem import PorterStemmer

def load_data(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

def preprocess_data(data):
    stemmer = PorterStemmer()
    words = []
    classes = []
    documents = []
    
    for intent in data['intents']:
        for pattern in intent['patterns']:
            # Tokenize and stem words
            word_list = nltk.word_tokenize(pattern)
            words.extend([stemmer.stem(word.lower()) for word in word_list])
            documents.append((word_list, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
    
    # Remove duplicates
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))
    
    return words, classes, documents
