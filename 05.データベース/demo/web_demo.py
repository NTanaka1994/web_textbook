from flask import Flask, request, redirect, render_template
import MySQLdb
import html
import datetime

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
def root_page():
    return redirect("home")

@app.route("/home", methods=["GET","POST"])
def title_page():
    if request.method == "GET":#GETメソッドの場合
        if request.args.get("word") is not None:#検索された場合は検索結果一覧を表示する
            word = request.args.get("word")
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        SELECT thread_id,title,intro,create_date 
                        FROM thread 
                        WHERE intro like %(intro)s OR title like %(title)s
                        """, {"intro":"%"+word+"%", "title":"%"+word+"%"})
            res = ""
            for col in cur:
                res = res + "<tr><td><a href=\"thread?id="+ html.escape(str(col[0])) +"\">" + html.escape(col[1]) + "</a></td>"
                res = res + "<td>" + html.escape(str(col[3])) + "</td></tr>"
                res = res + "<tr><td colspan=\"2\"><pre>" + html.escape(col[2]) +"</pre></td></tr>"
            con.close()
            return render_template("title.html", page_tite=html.escape(word)+"の検索結果", result=res)
        else:#検索されていない場合は一覧を表示しない
            return render_template("title.html", page_title="ホーム画面")
    elif request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    INSERT INTO thread 
                    (title,intro,create_date) 
                    VALUES (%(title)s,%(intro)s,%(create_date)s)
                    """, {"title":title, "intro":intro, "create_date":str(datetime.datetime.today())})
        con.commit()
        con.close()
        return redirect("home?word="+html.escape(title))

@app.route("/thread", methods=["GET","POST"])
def thread_page():
    if request.method == "GET":
        if request.args.get("id") is None:
            return redirect("home")
        else:
            thread_id=request.args.get("id")
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        SELECT title 
                        FROM thread
                        WHERE thread_id=%(thread_id)s
                        """,{"thread_id":html.escape(thread_id)})
            title = ""
            for row in cur:
                title = row[0]
            con.close()
            con = connect()
            cur = con.cursor()
            cur.execute("""
                        SELECT comment,send_date 
                        FROM comment
                        WHERE thread_id=%(thread_id)s
                        """,{"thread_id":html.escape(thread_id)})
            res = ""
            for row in cur:
                res = res + "<tr><td>投稿日時:" + html.escape(str(row[1])) + "</td></tr>\n"
                res = res + "<tr><td><pre>" + html.escape(row[0]) + "</pre></td></tr>\n"
            con.close()
            return render_template("comment.html", thread_id=thread_id, result=res, title=title)
    elif request.method == "POST":
        cont = request.form["cont"]
        thread_id = request.form["id"]
        con = connect()
        cur = con.cursor()
        cur.execute("""
                    INSERT INTO comment 
                    (thread_id,comment,send_date) 
                    VALUES (%(thread_id)s,%(comment)s,%(send_date)s)
                    """,{"thread_id":thread_id, "comment":cont, "send_date":str(datetime.datetime.today())})
        con.commit()
        con.close()
        return redirect("thread?id="+html.escape(str(thread_id)))

if __name__ == "__main__":
    app.run(host="0.0.0.0")