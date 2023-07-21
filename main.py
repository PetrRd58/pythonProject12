import requests

params = {"q" : "amsterdam"}
response = requests.get("https://trends.google.com//trends/explore",params=params)
#print(response.status_code)
#print(response.headers)
print(response.text)
