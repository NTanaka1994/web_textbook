from flask import Flask, request, render_template, redirect
import html

app = Flask(__name__)

@app.route("/")
def root():
    return redirect("home")

@app.route("/home")
def home():
    return render_template("form.html")

@app.route("/kai")
def kai():
    a = 0
    b = 0
    c = 0
    if request.args.get("a") is not None:
        try:
            a = float(request.args.get("a"))
        except:
            _ = 0
    if request.args.get("b") is not None:
        try:
            b = float(request.args.get("b"))
        except:
            _ = 0
    if request.args.get("c") is not None:
        try:
            c = float(request.args.get("c"))
        except:
            _ = 0
    D = (b ** 2) - 4 * a * c
    if D < 0:
        x = str(-b/(2*a))
        i = str(((-D)**0.5)/2*a)
        return render_template("kai.html", form="異なる二つの虚数解",
                               x1=html.escape("x1="+x+"-"+i+"i"),
                               x2=html.escape("x2="+x+"+"+i+"i"))
    elif D == 0:
        x = str(-b/(2*a))
        return render_template("kai.html", form="重解",x1=html.escape(x))
    elif D > 0:
        x1 = str(-b/(2*a)+(D**0.5)/(2*a))
        x2 = str(-b/(2*a)-(D**0.5)/(2*a))
        return render_template("kai.html", form="異なる二つの実数解", x1=html.escape(x1), x2=html.escape(x2))

if __name__ == "__main__":
    app.run(host="0.0.0.0")