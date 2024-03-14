from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<a href=\"download\">success.pdfのダウンロード</a>"

@app.route("/download")
def dl():
    return send_file("success.pdf")

if __name__ == "__main__":
    app.run(port=80)