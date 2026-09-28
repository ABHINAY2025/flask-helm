from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask API is running"
    })


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello, Abhinay!"
    })


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({
            "error": "name and email are required"
        }), 400

    return jsonify({
        "message": "User created successfully",
        "user": {
            "name": name,
            "email": email
        }
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
