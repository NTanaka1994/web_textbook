from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ajax_test.html")

@app.route("/ajax")
def ajax():
    return "<h2>非同期通信成功</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")