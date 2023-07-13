from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)

CORS(app)

#App route
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        "message": "Hello World!",
        "people" : ['Jack', 'Harry', 'Barry']
        })

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    