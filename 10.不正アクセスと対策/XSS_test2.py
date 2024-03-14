from flask import Flask, session, request, redirect, render_template
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
import datetime
import MySQLdb
import secrets

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

@app.route("/home", methods=["GET", "POST"])
def home():
    if "name" in session:
        if request.method == "GET":
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        SELECT comment,send_date 
                        FROM comment
                        """)
            res = "<form method=\"POST\" action=\"home\">\n"
            res = res + "\t<textarea name=\"cont\"></textarea>\n"
            res = res + "\t<input type=\"submit\" value=\"送信\">\n"
            res = res + "</form>"
            res = res + "<table>\n"
            for row in cur:
                res = res + "\t<tr><td>投稿日時</td><td>" + str(row[1]) + "</td></tr>\n"
                res = res + "\t<tr><td colspan=\"2\"><pre>" + row[0] + "</pre></tr>\n"
            res = res + "</table>\n"
            con.close()
            return res
        elif request.method == "POST":
            cont = request.form["cont"]
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        INSERT INTO comment 
                        (thread_id,comment,send_date) 
                        VALUES (%(thread_id)s,%(comment)s,%(send_date)s)
                        """,{"thread_id" : 100, "comment" : cont, "send_date" : str(datetime.datetime.today())})
            con.commit()
            con.close()
            return redirect("home")
    else:
        return redirect("login")

@app.route("/xss")
def xss():
    return str(request.args.get("id"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")