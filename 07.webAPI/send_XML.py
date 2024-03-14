from flask import Flask
import dicttoxml

app = Flask(__name__)

@app.route("/")
def send_xml():
    dic = {}
    dic["int"] = int(1)
    dic["float"] = float(1.23)
    dic["Null"] = None
    dic["string"] = "abc"
    dic["arr"] = [0, 1, 2, 3]
    dic["dic"] = {"1" : 1, "a" : "a"}
    xml = dicttoxml.dicttoxml(dic)
    res = app.make_response(xml)
    res.mimetype = "text/xml"
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0")