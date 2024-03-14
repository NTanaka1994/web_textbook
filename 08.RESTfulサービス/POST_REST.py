from flask import Flask, jsonify
import dicttoxml
import html
import pandas as pd

df = pd.read_csv("KEN_ALL_ROME.CSV",encoding="shift-jis")

app = Flask(__name__)

@app.route("/")
def rot():
    arr = df["J_state"].values
    arr = list(set(arr))
    res = ""
    for i in range(len(arr)):
        res = res + "<p><a href=\"" + arr[i] + "\">" + arr[i] + "</p>\n"
    return res

@app.route("/<town>")
def tow(town):
    res = "<h1>" + html.escape(town) + "の一覧</h1><a href=\"..\">\n"
    df_town = df.query("J_state=='%s'"%(town))
    city = df_town["J_city"].values
    city = list(set(city))
    res = res + "<table border=\"1\">\n"
    res = res + "\t<tr><th>都道府県</th><th>市区町村</th><th>HTML</th><th>JSON</th><th>XML</th>\n"
    for i in range(len(city)):
        res = res + "\t<tr><td>" + html.escape(town) + "</td><td>" + html.escape(city[i]) +"</td>"
        res = res + "<td><a href=\"" + html.escape(town) + "/" + html.escape(city[i]) + "/HTML" + "\">"
        res = res + "HTML</a></td>"
        res = res + "<td><a href=\"" + html.escape(town) + "/" + html.escape(city[i]) + "/JSON" + "\">"
        res = res + "JSON</a></td>"
        res = res + "<td><a href=\"" + html.escape(town) + "/" + html.escape(city[i]) + "/XML" + "\">"
        res = res + "XML</a></td>"
    res = res + "</table>"
    return res

@app.route("/<town>/<city>")
def cit(town, city):
    res = "<h1>" + html.escape(town) + html.escape(city) + "の一覧</h1>\n"
    df_town = df.query("J_state=='%s' and J_city=='%s'"%(town, city))
    num = df_town["ID"].values
    loc = df_town["J_loc"].values
    res = res + "<table border=\"1\">\n"
    res = res + "\t<tr><th>都道府県</th><th>市区町村</th><th>番地</th><th>郵便番号</th>\n"
    for i in range(len(num)):
        res = res + "\t<tr><td>" + html.escape(town) + "</td><td>" + html.escape(city)
        res = res + "</td><td>" + html.escape(loc[i]) + "</td><td>" + html.escape(str(num[i]))
        res = res + "</td></tr>"
    res = res + "</table>"
    return res

@app.route("/<town>/<city>/<form>")
def api(town, city, form):
    if form == "HTML" or form != "JSON" and form != "XML":
        res = "<h1>" + html.escape(town) + html.escape(city) + "の一覧</h1>\n"
        df_town = df.query("J_state=='%s' and J_city=='%s'"%(town, city))
        num = df_town["ID"].values
        loc = df_town["J_loc"].values
        res = res + "<table border=\"1\">\n"
        res = res + "\t<tr><th>都道府県</th><th>市区町村</th><th>番地</th><th>郵便番号</th>\n"
        for i in range(len(num)):
            res = res + "<tr><td>" + html.escape(town) + "</td><td>" + html.escape(city)
            res = res + "</td><td>" + html.escape(loc[i]) + "</td><td>" + html.escape(str(num[i]))
            res = res + "</td></tr>"
        res = res + "</table>"
        return res
    else:
        res = {}
        df_town = df.query("J_state=='%s' and J_city=='%s'"%(town, city))
        num = df_town["ID"].values
        loc = df_town["J_loc"].values
        tmpa = []
        res["place"] = town + city
        for i in range(len(num)):
            tmpd = {}
            tmpd["loc"] = loc[i]
            tmpd["num"] = int(num[i])
            tmpa.append(tmpd)
        res["loc_info"] = tmpa
        if form == "XML":
            xml = dicttoxml.dicttoxml(res)
            resp = app.make_response(xml)
            resp.mimetype = "text/xml"
            return resp
        elif form == "JSON":
            return jsonify(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0")