import json
import requests

def parse(jsn, var=""):
    if isinstance(jsn, dict):
        for row in jsn:
            parse(jsn[row], var=var+"[\""+row+"\"]")
    elif isinstance(jsn, list):
        for i in range(len(jsn)):
            parse(jsn[i], var=var+"["+str(i)+"]")
    else:
        print(var+"="+str(jsn))
        return var

url = "" #ここにJSONのあるURLを入れる

res = requests.get(url)

data = json.loads(res.text)

parse(data, "data")