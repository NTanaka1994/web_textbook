from flask import Flask, session, request, redirect, render_template
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
import secrets
import html
import MySQLdb

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
app.secret_key = secrets.token_urlsafe(16)
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route("/")
def root():
    return redirect("login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session.clear()
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form["email"]
        passwd = request.form["passwd"]
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT passwd,name,email,tel 
                    FROM users 
                    WHERE email=%(email)s
                    """,{"email":email})
        data=[]
        for row in cur:
            data.append([row[0],row[1],row[2],row[3]])
        if len(data)==0:
            con.close()
            return render_template("login.html", msg="IDが間違っています")
        if cph(data[0][0], passwd):
            session["name"] = data[0][1]
            session["email"] = data[0][2]
            session["tel"] = data[0][3]
            con.close()
            return redirect("home")
        else:
            con.close()
            return render_template("login.html", msg="パスワードが間違っています")

@app.route("/home")
def home():
    if "name" in session:
        return render_template("CSRF_home.html", user_name=html.escape(session["name"]))
    else:
        return redirect("login")

@app.route("/money", methods=["GET", "POST"])
def csrf():
    if "name" in session:
        bank = request.form["bank"]
        src = request.form["src"]
        val = request.form["val"]
        res = "<h1 align=\"center\">以下の通り振り込まれました</h1>\n"
        res = res + "<table align=\"center\">\n"
        res = res + "\t<tr><td align=\"right\">振込者</td><td>" + html.escape(session["name"]) + "</td>\n"
        res = res + "\t<tr><td align=\"right\">金融機関名</td><td>" + html.escape(bank) + "</td>\n"
        res = res + "\t<tr><td align=\"right\">送金先口座番号</td><td>" + html.escape(src) + "</td>\n"
        res = res + "\t<tr><td align=\"right\">金額</td><td>" + html.escape(val) + "円</td>\n"
        res = res + "</table>"
        return res
    else:
        return redirect("login") 

if __name__ == "__main__":
    app.run(host="0.0.0.0")