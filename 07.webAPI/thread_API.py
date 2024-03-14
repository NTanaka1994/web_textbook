from flask import Flask, request, jsonify, render_template
import dicttoxml
import MySQLdb
import html

def connect():
    con = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="abc",
        db="sample",
        use_unicode=True,
        charset="utf8")
    return con

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("search.html")

@app.route("/result")
def result():
    form = request.args.get("format")
    name = request.args.get("name")
    con = connect()
    cur = con.cursor()
    cur.execute("""
                SELECT thread_id,title,intro 
                FROM thread 
                WHERE title like %(title)s OR intro like %(intro)s
                """, {"title" : "%"+name+"%", "intro" : "%"+name+"%"})
    res = "<title>検索結果</title>"
    for row in cur:
        res = res + "<table border=\"1\">\n"
        res = res + "\t<tr><td><a href=\"api?id=" + html.escape(str(row[0])) + "&"
        res = res + "format=" + html.escape(form) + "\">" + html.escape(row[1]) + "</a></td></tr>\n"
        res = res + "\t<tr><td><pre>" + html.escape(row[2]) + "</pre></td></tr>"
        res = res + "</table>"
    con.close()
    return res

@app.route("/api")
def api():
    num = request.args.get("id")
    form = request.args.get("format")
    con = connect()
    cur = con.cursor()
    cur.execute("""
                SELECT comment_id,comment,send_date 
                FROM comment 
                WHERE thread_id=%(id)s
                """, {"id" : num})
    cur2 = con.cursor()
    cur2.execute("""
                 SELECT title
                 FROM thread
                 WHERE thread_id=%(id)s
                 """, {"id" : num})
    res = {}
    for row2 in cur2:
        res["title"] = row2[0]
    tmpa=[]
    for row in cur:
        tmpd={}
        tmpd["comment_id"] = row[0]
        tmpd["comment"] = row[1]
        tmpd["send_date"] = row[2]
        tmpa.append(tmpd)
    res["content"] = tmpa
    if form == "XML":
        xml = dicttoxml.dicttoxml(res)
        resp = app.make_response(xml)
        resp.mimetype = "text/xml"
        return resp
    else:
        return jsonify(res)
        
if __name__ == "__main__":
    app.run(host="0.0.0.0")