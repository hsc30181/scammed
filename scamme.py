import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """Congratulations, Mr. Sissons. You have been tricked by me! hahaha
    Credit @ Hyunsoo Cho, developer's comment: I made this myself when you weren't here hahaha
    Powered by Render (Render.com)"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives this dynamically
    app.run(host="0.0.0.0", port=port, debug=False)

