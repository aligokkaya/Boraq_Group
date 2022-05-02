import requests

r=requests.get('http://192.168.0.111:5000/v1/boraq/news')

print(r.text)