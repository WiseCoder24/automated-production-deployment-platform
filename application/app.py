
import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = "DevOps Status App"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": APP_NAME,
        "message": "DevOps Platform is running!",
        "version": APP_VERSION,
        "status": "running"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "application": APP_NAME,
        "version": APP_VERSION
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=False
    )
