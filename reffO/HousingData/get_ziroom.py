from bs4 import BeautifulSoup
import requests
import csv
import time
import os


def get_in_page_information(page):
    url = 'http://www.ziroom.com/z/nl/z3.html?p='+ str(page)
    # web_data = requests.get(url)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    web_data = requests.get(url=url, headers=header_dict)
    # print(web_data.text)
    web_data.encoding = 'utf-8'
    beautifulsoup = BeautifulSoup(web_data.text, 'lxml')

    """
    Adding your edit as an answer so that it can be more easily found by others:
    Use nth-of-type instead of nth-child:
    soup.select("#names > p:nth-of-type(1)")
    print(beautifulsoup.select('#houseList > li:nth-of-type(6)'))
    """
    for i in range(2,19):
        id = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ')> div.txt > h3 > a')[0].get('href').split('/')[-1].split('.')[0]
        # 地址 #houseList > li:nth-child(2) > div.txt > h3 > a
        area = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ')> div.txt > h3 > a')[0].text
        # 详细地址 #houseList > li:nth-child(2) > div.txt > h4 > a
        address = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ')> div.txt > h4 > a')[0].text
        # 详细信息 #houseList > li:nth-child(2) > div.txt > div > p:nth-child(1)
        information = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ')> div.txt > div > p:nth-of-type(1)')[0].text.replace('\n','').replace(' ','').split('|')
        information.append(information[-1][-1]) # 加入是否是合租信息
        information[2] = information[2][:-1]    # 去掉 4室1厅合 的最后一个字
        # 距离地铁站的距离 #houseList > li:nth-child(2) > div.txt > div > p:nth-child(2) > span
        distance_from_subway = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ') > div.txt > div > p:nth-of-type(2) > span')[0].text
        # 价格 #houseList > li:nth-child(2) > div.priceDetail > p.price
        price = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ') > div.priceDetail > p.price')[0].text.replace('\n','').replace(' ','')
        # 特点 #houseList > li:nth-child(2) > div.txt > p
        feature = beautifulsoup.select('#houseList > li:nth-of-type(' + str(i) + ') > div.txt > p')[0].text
        feature = feature.split('\n')
        while '' in feature:    # 去除空格
            feature.remove('')

        # print(id)
        # print(area)
        # print(address)
        # print(information)
        # print(distance_from_subway)
        # print(price)
        # print(feature)


        # file_write.writerow(['id', 'area', 'address', 'information', 'distance_from_subway', 'price', 'feature'])
        file_write.writerow([id, area, address, information, distance_from_subway, price, feature])

# get_in_page_information(1)
# print('================')
# get_in_page_information(2)
# 总共50页，第一次测量，全部抓取，没有sleep
os.mkdir('./ziroom')
file = open('./ziroom/' + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + '.csv', 'w', newline='')
file_write = csv.writer(file, dialect='excel')
file_write.writerow(['id', 'area', 'address', 'information', 'distance_from_subway', 'price', 'feature'])
for _ in range(1,51):
    print('Downloading page:' + str(_))
    get_in_page_information(_)
file.close()

