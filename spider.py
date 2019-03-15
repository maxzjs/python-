# -*- coding: gb2312 -*-
# maxzjs
# 2019.3.13


'''
14shucheng.com
爬取小说，有下载接口，直接用
'''

import os
import re
import requests
from bs4 import BeautifulSoup



def headerss(url):
    headers = {
        'Host': 'www.14shucheng.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': url,
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    return headers


faillist_down = []
faillist_do = []
title_down = []
url = 'https://www.14shucheng.com/top/3/0/'

def start():
    linklist = []
    for i in range(1,6000):
        response = requests.get(url + str(i) + '.html')
        print("正在爬取第"+str(i)+"页")
        soup = BeautifulSoup(response.text,'html.parser')
        for x in soup.find("div",attrs={'class':'list'}).find_all("a"):
            link = x.get('href')
            if re.findall(r'book',link):
                linklist.append(link)
                linklist = list(set(linklist))
        for y in linklist:

            second(y)

def second(url):
    link2list = []
    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.text,'html.parser')
    print('正在获取下载列表')
    for a in soup2.find_all("a",attrs={'target':'_blank'}):
        b = soup2.find("h1")
        title = b.get_text()
        link2 = a.get('href')
        if re.findall(r'download',link2):
           third(link2)






def third(url):
    respon = requests.get(url)
    soupp = BeautifulSoup(respon.text,'html.parser')
    title = soupp.find('h1').get_text()
    print('正在获取下载链接')
    for b in soupp.find_all("a"):
        link = b.get('href')
        if re.findall(r'down.php',link):
            #print(link)
            if re.findall(r'NULL',link):
                pass
            else:
                #print(link)
                forth(link,url,title)


def forth(url,url2,title):
    response_fina = requests.get(url,headers=headerss(url2))
    filename = str(title) + '.txt'
    if os.path.isfile(filename):
        print(filename,'已存在')
    else:
        with open(filename,'wb') as f:
            print('正在下载:',filename)
            f.write(response_fina.content)
        try:
            if os.path.getsize(filename) == 0:
                faillist_down.append(url)
                faillist_do.append(url2)
                title_down.append(title)

        except BaseException:
            print('出错了')






    # 下载文件，此时的url就是下载地址



start()
url2 = 'https://www.14shucheng.com/book/67915.html'
#second(url2)











