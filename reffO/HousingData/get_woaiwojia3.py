from bs4 import BeautifulSoup
import requests
import csv
import os
import time

def get_and_save():
    def get_in_page(url,page,type):

        url=url + str(page)
        req=requests.get(url)
        req.encoding='utf-8'
        soup=BeautifulSoup(req.text,'lxml')
        # print(req.text)
        print('==========================================================')
        acount_in_one_page = 31
        # if page > 4:
        #     acount_in_one_page = 27
        for i in range(1,acount_in_one_page):
            # print(i)
            # 编号 #exchangeList > div > ul > li:nth-child(1) > div > h2 > a
            id = soup.select('body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li:nth-of-type('+str(i)+') > div.listCon > h3 > a')[0].get('href').split('/')[-1].split('.')[0]
            # 总体信息：1 室 1 厅 · 57.23 平米 · 西南 · 中楼层/22层
            digest=soup.select('body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li:nth-of-type('+str(i)+') > div.listCon > div.listX > p:nth-of-type(1)')[0].text.replace(' ','')
            # [惠新西街 胜古家园,距离地铁站]
            location = soup.select('body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li:nth-of-type('+str(i)+') > div.listCon > div.listX > p:nth-of-type(2)')[0].text
            # body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li:nth-of-type('+str(i)+') > div.listCon > div.listX > div > p.redC > strong
            price = soup.select('body > div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li:nth-of-type('+str(i)+') > div.listCon > div.listX > div > p.redC > strong')[0].text
            print('id:' + id)
            print('digest:' +digest)
            print('location:' + str(location))
            print('price:' + price)
            print('type:' + type)
            print('----------------------------')
            file_write.writerow([id, digest, location, price, type])

    path = './woaiwojia/'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    file = open(path + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.csv', 'w', newline='')
    file_write = csv.writer(file, dialect='excel')
    file_write.writerow(['id', 'digest', 'ab_add2', 'ab_add3', 'size', 'chaoxiang', 'level','price','rent_type'])
    for _ in range(1, 36):
        print('Downloading page:' + str(_))
        try:
            get_in_page(url='https://bj.5i5j.com/zufang/n/u1n',page=_,type='整租')
        except:
            pass
    file.close()
