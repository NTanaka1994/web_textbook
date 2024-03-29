from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("GET_check.html")

@app.route("/result")
def result():
    arr1 = request.args.getlist("var1")
    text = "選択肢1で選択された内容<br>\n"
    for arr in arr1:
        text = text + html.escape(arr) + "<br>\n"
    arr2 = request.args.getlist("var2")
    text = text + "選択肢2で選択された内容<br>\n"
    for arr in arr2:
        text = text + html.escape(arr) + "<br>\n"
    return text

if __name__ == "__main__":
    app.run(host="0.0.0.0")