from flask import Flask, request, redirect, render_template
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
def root():
    return redirect("new")

@app.route("/new")
def new():
    return render_template("new_SQLinjection.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT name,sex,school,post FROM list")
        res = "<table align=\"center\">\n"
        res = res + "\t<tr><th>名前</th><th>性別</th><th>学校名</th><th>役職・立場</th>\n"
        for row in cur:
            res = res + "\t<tr><td>" + html.escape(str(row[0])) + "</td>"
            res = res + "<td>" + html.escape(row[1]) + "</td>"
            res = res + "<td>" + html.escape(row[2]) + "</td>"
            res = res + "<td>" + html.escape(row[3]) + "</td>"
        res = res + "</table>"
        con.close()
        return res
    elif request.method == "POST":
        name = request.form["name"]
        post = request.form["post"]
        sex = request.form["sex"]
        school = request.form["school"]
        con = connect()
        
        cur = con.cursor()
        cur.execute("""
                    INSERT INTO list 
            (sex,school,post,name) VALUES 
            ('""" + sex + """','""" + school + """','""" + post + """','""" + name + """')
                    """)
        con.commit()
        con.close()
        return redirect("home")

if __name__ == "__main__":
    app.run(host="0.0.0.0")