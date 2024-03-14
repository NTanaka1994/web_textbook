from flask import Flask
import html

app = Flask(__name__)

@app.route("/<var>")
def one_var(var):
    return "var = " + html.escape(var)

@app.route("/<var_1>/<var_2>")
def two_var(var_1, var_2):
    return "var_1 = " + html.escape(var_1) + "<br>var_2 = " + html.escape(var_2)

if __name__ == "__main__":
    app.run("0.0.0.0")