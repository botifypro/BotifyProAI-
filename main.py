from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "BotifyProAI activo"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
