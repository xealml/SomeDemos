import requests
import getSig2

file = open("ips.csv",'r')

iplist = []
for _ in file:

    # print(_.replace('\n','').split(',')[1:])
    for __ in _.replace('\n','').split(',')[1:]:
        # print(__)
        iplist.append(__)
    # iplist.append(__ for __ in _.replace('\n','').split(',')[1:])
print(iplist)


count = 0
for _ in iplist:
    url = "http://" + _ +":80/time/files/shell.php"

    try:
        r = requests.get(url)
    except:
        pass
    if r.status_code == 200:
        count += 1
        print(url , r.status_code)


print(count)