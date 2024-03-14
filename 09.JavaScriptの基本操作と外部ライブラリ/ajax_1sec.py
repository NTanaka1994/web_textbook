from flask import Flask, request, render_template
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ajax_count.html")

@app.route("/ajax")
def count():
    sec = int(request.args.get("sec"))
    return html.escape(str(sec + 1))

if __name__ == "__main__":
    app.run(host="0.0.0.0")