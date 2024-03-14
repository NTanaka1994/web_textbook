from flask import Flask, send_file, redirect, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("home")

@app.route("/home")
def home():
    return render_template("directory.html")

@app.route("/file")
def file():
    name = os.path.basename(request.args.get("name"))
    file = "static/public/" + name
    return send_file(file)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")