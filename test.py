import requests

r=requests.get('http://127.0.0.1/v1/boraq/news')

print(r.text)