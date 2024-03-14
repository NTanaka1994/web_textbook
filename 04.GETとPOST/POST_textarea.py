from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("POST_textarea.html")

@app.route("/result", methods=["POST"])
def result():
    text = request.form["var"]
    return "<pre>" + html.escape(text) + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")