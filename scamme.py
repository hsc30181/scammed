import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("Congratulations, Mr. Sissons! You have been tricked!")
    return "Check your console log!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives this dynamically
    app.run(host="0.0.0.0", port=port, debug=False)
