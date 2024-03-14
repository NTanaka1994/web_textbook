from flask import Flask, session, request, redirect, render_template
from datetime import timedelta
import datetime
import MySQLdb
import secrets
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
app.secret_key = secrets.token_urlsafe(16)
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route("/")
def root():
    return redirect("login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session.clear()
        return render_template("login_SQLinjection.html")
    elif request.method == "POST":
        email = request.form["email"]
        passwd = request.form["passwd"]
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT email,name FROM users WHERE email='%s' AND passwd='%s'"%(email, passwd))
        data=[]
        for row in cur:
            data.append([row[0],row[1]])
        if len(data)==0:
            con.close()
            return render_template("login_SQLinjection.html", msg="IDかパスワードが間違っています")
        else:
            session["email"] = data[0][0]
            session["name"] = data[0][1]
            con.close()
            return redirect("home")

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
                res = res + "\t<tr><td>投稿日時</td><td>" + html.escape(str(row[1])) + "</td></tr>\n"
                res = res + "\t<tr><td colspan=\"2\"><pre>" + html.escape(row[0]) + "</pre></tr>\n"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")