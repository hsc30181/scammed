from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("Congratulations, Mr. Sissons! You have been scammed!")
    print("Credit @Jacob, developer's comment: I made this Mr. Sissons haha")
    return "Press F12!(Don't worry. I made this myself and it's totally safe.)"

if __name__ == "__main__":
    app.run(debug=False)
