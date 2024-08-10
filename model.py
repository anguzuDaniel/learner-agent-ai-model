from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
import numpy as np

def create_model(input_shape, output_shape):
    model = Sequential([
        Dense(8, input_shape=(input_shape,), activation='relu'),
        Dense(8, activation='relu'),
        Dense(output_shape, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, x_train, y_train, epochs=1000, batch_size=8):
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)
    model.save('learner_agent_model.keras')

def load_trained_model(model_path):
    return load_model(model_path)

def predict_class(sentence, words, model):
    # Convert input to bag of words
    bag = np.array([1 if word in sentence else 0 for word in words]).reshape(1, -1)
    prediction = model.predict(bag)
    return np.argmax(prediction)

def get_response(predicted_class, classes, data):
    tag = classes[predicted_class]
    for intent in data['intents']:
        if intent['tag'] == tag:
            return np.random.choice(intent['responses'])
    return "Sorry, I don't understand."
