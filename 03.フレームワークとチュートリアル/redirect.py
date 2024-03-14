from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def rooturl():
    return redirect("hello_world")

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")