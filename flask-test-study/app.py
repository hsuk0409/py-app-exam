from flask import Flask, request, jsonify


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    @app.route("/hello", methods=["POST"])
    def hello():
        payload = request.json
        message = f"hello, {payload['name']}"
        return jsonify({
            "message": message
        })

    return app