from flask import Flask, render_template, request, redirect
import requests
import json
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate")
def gene():
    if request.args.get("postnum") is not None:
        num = request.args.get("postnum")
        param = {
                "method" : "searchByPostal",
                "postal" : num
        }
        url = "https://geoapi.heartrails.com/api/json"
        res = requests.get(url, params=param)
        jsn = json.loads(res.text)
        marker = ""
        x = []
        y = []
        for i in range(len(jsn["response"]["location"])):
            marker = marker + "\t\t\t\tL.marker([" + html.escape(str(jsn["response"]["location"][i]["y"]))
            marker = marker + ", " + html.escape(str(jsn["response"]["location"][i]["x"])) + "])"
            marker = marker + ".bindPopup(\"" + html.escape(jsn["response"]["location"][i]["prefecture"])
            marker = marker + html.escape(jsn["response"]["location"][i]["city"])
            marker = marker + html.escape(jsn["response"]["location"][i]["town"])
            marker = marker + "\").addTo(map);\n"
            x.append(float(jsn["response"]["location"][i]["x"]))
            y.append(float(jsn["response"]["location"][i]["y"]))
        cx = sum(x) / len(x)
        cy = sum(y) / len(y)
        marker = marker + "\t\t\t\tL.marker([" + str(cy) + ", " + str(cx) + "]).bindPopup(\""
        marker = marker + num + "\").addTo(map);\n"
        return render_template("map_generate.html", y=cy, x=cx, marker=marker, num=num)
    else:
        return redirect("..")

if __name__ == "__main__":
    app.run(host="0.0.0.0")