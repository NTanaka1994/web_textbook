from flask import Flask,render_template
import pandas as pd
import json
import requests

df=pd.read_csv("KEN_ALL_ROME.CSV",encoding="shift-jis")

app = Flask(__name__)

@app.route("/")
def rot():
    arr=df["J_state"].values
    arr=list(set(arr))
    res=""
    for i in range(len(arr)):
        res=res+"<p><a href=\""+arr[i]+"\">"+arr[i]+"</p>\n"
    return res

@app.route("/loc/<postnum>")
def loc(postnum):
    url="http://geoapi.heartrails.com/api/json?method=searchByPostal&postal="+str(postnum)
    res=requests.get(url)
    jsn=json.loads(res.text)
    dic=jsn["response"]["location"]
    marker=""
    x=[]
    y=[]
    for i in range(len(dic)):
        marker=marker+"L.marker(["+str(jsn["response"]["location"][i]["y"])+", "+str(jsn["response"]["location"][i]["x"])+"],{title:\""+jsn["response"]["location"][i]["town"]+"\"}).addTo(map);\n"
        x.append(float(jsn["response"]["location"][i]["x"]))
        y.append(float(jsn["response"]["location"][i]["y"]))
    return render_template("loc.html",num=str(postnum),x=str(sum(x)/len(x)),y=str(sum(y)/len(y)),marker=marker)

@app.route("/<town>")
def tow(town):
    res="<h1>"+town+"の一覧</h1>\n"
    df_town=df.query("J_state=='%s'"%(town))
    num=df_town["ID"].values
    city=df_town["J_city"].values
    loc=df_town["J_loc"].values
    res=res+"<table border=\"1\">\n"
    res=res+"\t<tr><th>都道府県</th><th>市区町村</th><th>番地</th><th>郵便番号</th>\n"
    for i in range(len(num)):
        res=res+"<tr><td>"+town+"</td><td><a href=\""+town+"/"+city[i]+"\">"+city[i]+"</a></td><td>"+loc[i]+"</td><td><a href=\"loc/"+str(num[i])+"\">"+str(num[i])+"</a></td></tr>"
    res=res+"</table>"
    return res

@app.route("/<town>/<city>")
def cit(town,city):
    res="<h1>"+town+city+"の一覧</h1>\n"
    df_town=df.query("J_state=='%s' and J_city=='%s'"%(town,city))
    num=df_town["ID"].values
    loc=df_town["J_loc"].values
    res=res+"<table border=\"1\">\n"
    res=res+"\t<tr><th>都道府県</th><th>市区町村</th><th>番地</th><th>郵便番号</th>\n"
    for i in range(len(num)):
        res=res+"<tr><td>"+town+"</td><td>"+city+"</td><td>"+loc[i]+"</td><td><a href=\"../loc/"+str(num[i])+"\">"+str(num[i])+"</a></td></tr>"
    res=res+"</table>"
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0")