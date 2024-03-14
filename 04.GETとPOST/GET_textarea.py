from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("GET_textarea.html")

@app.route("/result")
def result():
    text = request.args.get("var")
    return "<pre>" + html.escape(text) + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")