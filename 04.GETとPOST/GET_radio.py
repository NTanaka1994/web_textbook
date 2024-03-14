from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("GET_radio.html")

@app.route("/result")
def result():
    sel1 = request.args.get("var1")
    text = "選択肢1で選択された内容<br>\n"
    text = text + html.escape(sel1) + "<br>\n"
    sel2 = request.args.get("var2")
    text = text + "選択肢2で選択された内容<br>\n"
    text = text + html.escape(sel2) + "<br>\n"
    return text

if __name__ == "__main__":
    app.run(host="0.0.0.0")