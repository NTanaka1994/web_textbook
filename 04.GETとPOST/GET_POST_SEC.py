from flask import Flask,render_template,session,request
import html

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

"""
@app.route("/GET_NON_SEC")
def gns():
    res="<table>\n"
    res=res+"\t<tr><td>テキストボックスの文字列</td><td>"+request.args.get("text")+"</td></tr>\n"
    res=res+"\t<tr><td>数字テキストボックスの文字列</td><td>"+request.args.get("number")+"</td></tr>\n"
    res=res+"\t<tr><td>日付の文字列</td><td>"+str(request.args.get("date"))+"</td></tr>\n"
    res=res+"\t<tr><td>ラジオボタン1の値</td><td>"+request.args.get("radio1")+"</td></tr>\n"
    res=res+"\t<tr><td>ラジオボタン2の値</td><td>"+request.args.get("radio1")+"</td></tr>\n"
    res=res+"\t<tr><td>チェックボックス1のチェック項目</td><td>"+str(request.args.getlist("check1"))+"</td></tr>\n"
    res=res+"\t<tr><td>チェックボックス2のチェック項目</td><td>"+str(request.args.getlist("check2"))+"</td></tr>\n"
    res=res+"\t<tr><td>隠し要素の文字列</td><td>"+request.args.get("hidden")+"</td></tr>\n"
    res=res+"</table>"
    return res
"""

@app.route("/GET_SEC")
def gs():
    res="<table>\n"
    res=res+"\t<tr><td>テキストボックスの文字列</td><td>"+html.escape(request.args.get("text"))+"</td></tr>\n"
    res=res+"\t<tr><td>数字テキストボックスの文字列</td><td>"+html.escape(request.args.get("number"))+"</td></tr>\n"
    res=res+"\t<tr><td>日付の文字列</td><td>"+html.escape(str(request.args.get("date")))+"</td></tr>\n"
    res=res+"\t<tr><td>ラジオボタン1の値</td><td>"+html.escape(request.args.get("radio1"))+"</td></tr>\n"
    res=res+"\t<tr><td>ラジオボタン2の値</td><td>"+html.escape(request.args.get("radio1"))+"</td></tr>\n"
    res=res+"\t<tr><td>チェックボックス1のチェック項目</td><td>"+html.escape(str(request.args.getlist("check1")))+"</td></tr>\n"
    res=res+"\t<tr><td>チェックボックス2のチェック項目</td><td>"+html.escape(str(request.args.getlist("check2")))+"</td></tr>\n"
    res=res+"\t<tr><td>隠し要素の文字列</td><td>"+html.escape(request.args.get("hidden"))+"</td></tr>\n"
    res=res+"\t<tr><td>テキストエディタの内容</td><td><pre>"+html.escape(request.args.get("plaintext"))+"</pre></td></tr>\n"
    res=res+"</table>"
    return res
"""
@app.route("/POST_NON_SEC",methods=["POST"])
def pns():
    res="<table>\n"
    res=res+"\t<tr><td>テキストボックスの文字列</td><td>"+request.form["text"]+"</td></tr>\n"
    res=res+"\t<tr><td>数字テキストボックスの文字列</td><td>"+request.form["number"]+"</td></tr>\n"
    res=res+"\t<tr><td>日付の文字列</td><td>"+str(request.form["date"])+"</td></tr>\n"
    res=res+"\t<tr><td>ラジオボタン1の値</td><td>"+request.form["radio1"]+"</td></tr>\n"
    res=res+"\t<tr><td>ラジオボタン2の値</td><td>"+request.form["radio1"]+"</td></tr>\n"
    res=res+"\t<tr><td>チェックボックス1のチェック項目</td><td>"+str(request.form.getlist("check1"))+"</td></tr>\n"
    res=res+"\t<tr><td>チェックボックス2のチェック項目</td><td>"+str(request.form.getlist("check2"))+"</td></tr>\n"
    res=res+"\t<tr><td>隠し要素の文字列</td><td>"+request.form["hidden"]+"</td></tr>\n"
    res=res+"</table>"
    return res
"""
@app.route("/POST_SEC",methods=["POST"])
def ps():
    if request.form["csrf_check"]==session["home"]:
        res="<table>\n"
        res=res+"\t<tr><td>テキストボックスの文字列</td><td>"+html.escape(request.form["text"])+"</td></tr>\n"
        res=res+"\t<tr><td>数字テキストボックスの文字列</td><td>"+html.escape(request.form["number"])+"</td></tr>\n"
        res=res+"\t<tr><td>日付の文字列</td><td>"+html.escape(str(request.form["date"]))+"</td></tr>\n"
        res=res+"\t<tr><td>ラジオボタン1の値</td><td>"+html.escape(request.form["radio1"])+"</td></tr>\n"
        res=res+"\t<tr><td>ラジオボタン2の値</td><td>"+html.escape(request.form["radio1"])+"</td></tr>\n"
        res=res+"\t<tr><td>チェックボックス1のチェック項目</td><td>"+html.escape(str(request.form.getlist("check1")))+"</td></tr>\n"
        res=res+"\t<tr><td>チェックボックス2のチェック項目</td><td>"+html.escape(str(request.form.getlist("check2")))+"</td></tr>\n"
        res=res+"\t<tr><td>隠し要素の文字列</td><td>"+html.escape(request.form["hidden"])+"</td></tr>\n"
        res=res+"\t<tr><td>テキストエディタの内容</td><td><pre>"+html.escape(request.form["plaintext"])+"</pre></td></tr>\n"
        res=res+"</table>"
        return res
    else:
        res="<h1>不正なアクセスです</h1>"
        res=res+"<a href=\"..\">ホームに戻る</a>"
        return res

if __name__ == "__main__":
    app.run(host="0.0.0.0")