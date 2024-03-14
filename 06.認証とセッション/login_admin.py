from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
import html
import secrets
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
def start():
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
                    SELECT passwd,name,email,tel,admin 
                    FROM users 
                    WHERE email=%(email)s
                    """,{"email":email})
        data=[]
        for row in cur:
            data.append([row[0],row[1],row[2],row[3],row[4]])
        if len(data)==0:
            con.close()
            return render_template("login.html", msg="IDが間違っています")
        if cph(data[0][0], passwd):
            session["name"] = data[0][1]
            session["email"] = data[0][2]
            session["tel"] = data[0][3]
            session["admin"] = 0 if data[0][4] is None else data[0][4]
            con.close()
            return redirect("home")
        else:
            con.close()
            return render_template("login.html", msg="パスワードが間違っています")

@app.route("/home")
def home():
    if "name" in session:
        if session["admin"] == 1:
            return render_template("success.html", 
                                   name=html.escape(session["name"]), 
                                   email=html.escape(session["email"]), 
                                   tel=html.escape(session["tel"]), 
                                   admin="<a href=\"admin\">ユーザ情報一覧</a>")
        else:
            return render_template("success.html", 
                                   name=html.escape(session["name"]), 
                                   email=html.escape(session["email"]), 
                                   tel=html.escape(session["tel"]))
    else:
        return redirect("login")

@app.route("/admin")
def admin():
    if "admin" in session:
        if session["admin"] == 1:
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        SELECT name,email,tel 
                        FROM users
                        """)
            res=""
            for row in cur:
                res = res + "<table border=\"1\" align=\"center\">\n"
                res = res + "\t<tr><td align=\"right\">名前</td><td>" + html.escape(row[0]) + "</td></tr>\n"
                res = res + "\t<tr><td align=\"right\">メールアドレス</td><td>" + html.escape(row[1]) + "</td></tr>\n"
                res = res + "\t<tr><td align=\"right\">電話番号</td><td>" + html.escape(row[2]) + "</td></tr>\n"
                res = res + "</table>"
            con.close()
            return res
        else:
            return redirect("home")
    else:
        return redirect("login")
            
@app.route("/make", methods=["GET", "POST"])
def make():
    if request.method == "GET":
        return render_template("make.html")
    elif request.method == "POST":
        email = request.form["email"]
        passwd = request.form["passwd"]
        name = request.form["name"]
        tel = request.form["tel"]
        hashpass=gph(passwd)
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    SELECT * FROM users WHERE email=%(email)s
                    """,{"email":email})
        data=[]
        for row in cur:
            data.append(row)
        if len(data)!=0:
            return render_template("make.html", msg="既に存在するメールアドレスです")
        con.commit()
        con.close()
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    INSERT INTO users 
                    (email,passwd,tel,name) 
                    VALUES (%(email)s,%(hashpass)s,%(tel)s,%(name)s)
                    """,{"email":email, "hashpass":hashpass, "tel":tel, "name":name})
        con.commit()
        con.close()
        return render_template("info.html", email=email, passwd=passwd, name=name, tel=tel)

if __name__ == "__main__":
    app.run(host="0.0.0.0")