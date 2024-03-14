from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def send_json():
    dic = {}
    dic["int"] = int(1)
    dic["float"] = float(1.23)
    dic["Null"] = None
    dic["string"] = "abc"
    dic["arr"] = [0, 1, 2, 3]
    dic["dic"] = {"1" : 1, "a" : "a"}
    return jsonify(dic)

if __name__ == "__main__":
    app.run(host="0.0.0.0")