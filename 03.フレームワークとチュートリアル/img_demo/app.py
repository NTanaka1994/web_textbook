from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    res = "同じディレクトリに画像を保存した場合<br>\n"
    res = res + "<img src=\"success.png\" alt=\"同じディレクトリ\"><br>\n"
    res = res + "staticに画像を保存した場合<br>\n"
    res = res + "<img src=\"static/success.png\" alt=\"staticに保存した場合\">"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0")