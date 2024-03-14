from flask import Flask, send_file, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("home")

@app.route("/home")
def home():
    return render_template("directory.html")

@app.route("/file")
def file():
    name = request.args.get("name")
    file = "static/public/" + name
    pathlist = os.path.realpath(file).split("\\")
    if pathlist[-2] != "public" and pathlist[-3] == "static":
        return "<h1>不正なアクセスです</h1>"
    else:
        return send_file(file)

if __name__ == "__main__":
    app.run(host="0.0.0.0")