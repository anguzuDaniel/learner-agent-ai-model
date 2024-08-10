from flask import Flask, request, jsonify
from utils import recommend

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend_endpoint():
    user_input = request.json.get('input')
    recommendations = recommend(user_input)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
