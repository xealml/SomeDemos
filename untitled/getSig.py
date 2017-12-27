import requests
from bs4 import BeautifulSoup

def getsig():
    url = "http://172.16.100.4:4000/profile"
    headers = {'Cookie': 'MacaronSession=b5bc4edf212b7b92'}
    r = requests.get(url, headers=headers)
    # print(r.text)
    beautifulsoup = BeautifulSoup(r.text)
    string = beautifulsoup.select('#team-sig')[0].text
    print(string)
    return string