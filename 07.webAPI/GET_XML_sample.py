import requests
import xmltodict

url = "https://geoapi.heartrails.com/api/xml"
param = {
        "method" : "searchByPostal",
         "postal" : "1000001"
        }

res = requests.get(url, params=param)

data = xmltodict.parse(res.text)

x = data["response"]["location"]["x"]["#text"]
y = data["response"]["location"]["y"]["#text"]
name = data["response"]["location"]["prefecture"]
name = name + data["response"]["location"]["city"]
name = name + data["response"]["location"]["town"]

print("緯度:"+x)
print("経度:"+y)
print("住所:"+name)