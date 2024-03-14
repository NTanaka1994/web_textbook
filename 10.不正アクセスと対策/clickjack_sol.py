from flask import Flask, render_template, request, session, redirect
from werkzeug.security import check_password_hash as cph
from datetime import timedelta
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
def root():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        session.clear()
        return render_template("clickjack_login.html")
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
            return render_template("clickjack_login.html", msg="IDが間違っています")
        if cph(data[0][0], passwd):
            session["name"] = data[0][1]
            session["email"] = data[0][2]
            session["tel"] = data[0][3]
            con.close()
            return redirect("normal")
        else:
            con.close()
            return render_template("clickjack_login.html", msg="パスワードが間違っています")

@app.route("/normal")
def normal():
    if "name" in session:
        return "<h1>ログイン成功</h1>"
    else:
        return redirect("login")

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")