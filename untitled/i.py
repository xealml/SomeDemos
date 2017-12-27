import requests
url = "http://192.168.31.39:80"
r = requests.get(url)
print(r.status_code)