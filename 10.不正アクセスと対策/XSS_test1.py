from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    res = ""
    res = res + "<form method=\"POST\" action=\"test\">\n"
    res = res + "\t<input type=\"text\" name=\"XSS\">"
    res = res + "\t<input type=\"submit\" value=\"submit\">"
    return res

@app.route("/test", methods=["POST"])
def xss():
    return request.form["XSS"]

if __name__ == "__main__":
    app.run(host="0.0.0.0")