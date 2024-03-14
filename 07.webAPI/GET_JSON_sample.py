import requests
import json

url = "https://geoapi.heartrails.com/api/json"
param = {
        "method" : "searchByPostal",
         "postal" : "1000001"
        }

res = requests.get(url, params=param)

data = json.loads(res.text)

x = data["response"]["location"][0]["x"]
y = data["response"]["location"][0]["y"]
name = data["response"]["location"][0]["prefecture"]
name = name + data["response"]["location"][0]["city"]
name = name + data["response"]["location"][0]["town"]

print("緯度:"+x)
print("経度:"+y)
print("住所:"+name)