from flask import Flask, jsonify, render_template
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ajax_chart.html")

@app.route("/json")
def func3dim():
    x = np.linspace(-2, 2, 20)
    y = x ** 3 - 2 * x
    x = list(x)
    y = list(y)
    res = {}
    res["x"] = x
    res["y"] = y
    return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0")