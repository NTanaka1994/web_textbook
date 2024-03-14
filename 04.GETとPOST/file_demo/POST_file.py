from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("POST_file.html")

@app.route("/result", methods=["POST"])
def result():
    if "file" not in request.files:
        return "ファイルは送信されていません"
    file = request.files["file"]
    if file.filename == "":
        return "ファイル名が有りません"
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save("保存用フォルダ/"+filename)
    return "保存完了<br>\n<a href=\"..\">戻る</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")