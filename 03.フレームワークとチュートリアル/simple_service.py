from flask import Flask

app = Flask(__name__)

@app.route("/a")
def a_page():
    return "here is A<br>\n<a href=\"b\">to B</a>"

@app.route("/b")
def b_page():
    return "here is B<br>\n<a href=\"a\">to A</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")