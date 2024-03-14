from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("POST_text.html")

@app.route("/result", methods=["POST"])
def result():
    text = request.form["var"]
    return html.escape(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")