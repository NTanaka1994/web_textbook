from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("GET_text.html")

@app.route("/result")
def result():
    if request.args.get("var") is not None:
        text = request.args.get("var")
        return html.escape(text)
    else:
        return "テキストは送信されていない"

if __name__ == "__main__":
    app.run(host="0.0.0.0")