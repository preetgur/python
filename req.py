import requests

r = requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL")
print(r.status_code)
print(r.text)

# Post request is not cached
print("############ Post Request")

url_addres = "https://reqres.in/api/register"
data_send = {
    "email":"eve.holt@reqres.in",
    "password": "pistol"
}

r2 = requests.post(url=url_addres,data=data_send)
# r2 : recieve the response
import json
r2_json = r2.json()

print(r2.text)
print(type(r2),r2)
print(type(r2_json),r2_json)
print(r2_json["id"])

print(r2.headers)
