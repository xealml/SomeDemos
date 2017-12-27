from bs4 import BeautifulSoup
import requests
import csv
import os
import time

def get_and_save():
    def get_in_page(page):

        url='http://bj.5i5j.com/rent/n' + str(page)
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
            id = soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > h2 > a')[0].get('href').split('/')[-1]
            # 总体信息：荣丰2008 1室1厅2卫
            digest=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > h2 > a')[0].text
            # 大致坐标,属于冗余信息，包含在了总体信息的[0]的位置
            ab_add=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li:nth-of-type(1) > a:nth-of-type(1) > h3')[0].text
            # 属于哪个城区，西城还是丰台
            ab_add2=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li:nth-of-type(1) > a:nth-of-type(2)')[0].text
            # 小范围的分片
            ab_add3=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li:nth-of-type(1) > a:nth-of-type(3)')[0].text
            # 房屋大小
            size=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li.font-balck > span:nth-of-type(2)')[0].text
            # 朝向
            chaoxiang=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li.font-balck > span:nth-of-type(3)')[0].text
            # 层数
            level=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li.font-balck > span:nth-of-type(4)')[0].text
            # 价格
            price=soup.select('#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > div > h3')[0].text
            # 出租方式
            rent_type = soup.select('#exchangeList > div > ul > li:nth-of-type(' + str(i) + ') > div > div > p')[0].text.split('：')[-1]

            # print(id)
            # print(digest)
            # # print(ab_add)
            # print(ab_add2)
            # print(ab_add3)
            # print(size)
            # print(chaoxiang)
            # print(level)
            # print(price)
            # print(rent_type)
            file_write.writerow([id, digest, ab_add2, ab_add3, size, chaoxiang, level,price,rent_type])

    path = './woaiwojia/'
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    file = open(path + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.csv', 'w', newline='')
    file_write = csv.writer(file, dialect='excel')
    file_write.writerow(['id', 'digest', 'ab_add2', 'ab_add3', 'size', 'chaoxiang', 'level','price','rent_type'])
    for _ in range(1, 175):
        print('Downloading page:' + str(_))
        try:
            get_in_page(_)
        except:
            pass
    file.close()

#exchangeList > div > ul > li:nth-child(1) > div > ul > li:nth-child(1) > a:nth-child(1) > h3
#exchangeList > div > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a:nth-child(1) > h3
#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li:nth-child(1) > a:nth-child(2)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li:nth-child(1) > a:nth-child(3)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li.font-balck > span:nth-child(2)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li.font-balck > span:nth-child(3)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li.font-balck > span:nth-child(4)
#exchangeList > div > ul > li:nth-child(8) > div > div > h3
#exchangeList > div > ul > li:nth-child(8) > div > div > p