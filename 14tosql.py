# -*- coding:gb2312 -*-
# 2019.3.15
# maxzjs

import re,os
import requests
from bs4 import BeautifulSoup
import pymysql

url = 'https://www.14shucheng.com/top/3/0/'

def start():
    link1list = []
    for i in range(1,5746):
        response = requests.get(url + str(i) + '.html')
        print('正在爬取第'+str(i)+'页')
        soup1 = BeautifulSoup(response.text,'html.parser')
        for x in soup1.find("div",attrs={'class':'list'}).find_all("a"):
            link1 = x.get('href')
            if re.findall(r'book',link1):
                link1list.append(link1)
                link1list = list(set(link1list))
        for y in link1list:
            second(y)


def second(url):
    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.text,'html.parser')
    for a in soup2.find_all("a",attrs={'target':'_blank'}):
        b = soup2.find('h1')
        title = b.get_text()
        link2 = a.get('href')
        if re.findall(r'download',link2):
            third(link2,title)



def third(url,title):
    print(url,title)





start()



















