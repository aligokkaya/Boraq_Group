import http.client


def fetch_products(app):
    # api_key='3dSY5ixP987EcVVyXYbO6U:4GNeYKDpDDUGGuJac7wvdA'
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 3dSY5ixP987EcVVyXYbO6U:4GNeYKDpDDUGGuJac7wvdA"
        }

    conn.request("GET", "/news/getNews?country=tr&tag=general", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    return data.decode("utf-8")