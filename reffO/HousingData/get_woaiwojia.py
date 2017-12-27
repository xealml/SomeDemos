from bs4 import BeautifulSoup
import requests
import csv

def get_in_page(page):

    url='http://bj.5i5j.com/rent/n' + str(page)
    req=requests.get(url)
    req.encoding='utf-8'
    soup=BeautifulSoup(req.text,'lxml')
    # print(req.text)
    print('==========================================================')
    for i in range(1,31):
        print(i)
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

        print(digest)
        # print(ab_add)
        print(ab_add2)
        print(ab_add3)
        print(size)
        print(chaoxiang)
        print(level)
        print(price)
        print(rent_type)
        csv_file=open('test1.csv','a')
        writer=csv.writer(csv_file)
        writer.writerow([digest,ab_add2,ab_add3,size,chaoxiang,level,price,rent_type])
        csv_file.close()
#exchangeList > div > ul > li:nth-child(1) > div > ul > li:nth-child(1) > a:nth-child(1) > h3
#exchangeList > div > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a:nth-child(1) > h3
#exchangeList > div > ul > li:nth-of-type('+str(i)+') > div > ul > li:nth-child(1) > a:nth-child(2)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li:nth-child(1) > a:nth-child(3)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li.font-balck > span:nth-child(2)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li.font-balck > span:nth-child(3)
#exchangeList > div > ul > li:nth-child(8) > div > ul > li.font-balck > span:nth-child(4)
#exchangeList > div > ul > li:nth-child(8) > div > div > h3
#exchangeList > div > ul > li:nth-child(8) > div > div > p
get_in_page(1)
get_in_page(2)
get_in_page(3)
get_in_page(4)

