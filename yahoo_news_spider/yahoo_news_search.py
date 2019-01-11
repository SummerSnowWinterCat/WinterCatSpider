from bs4 import BeautifulSoup
import os
import urllib.request as urllib_request
import re
import ssl
import fake_user
import lxml

url = 'https://news.yahoo.co.jp/list/'


def get_search_data():
    headers = {'User-Agent': fake_user.get_fake_user()}
    search_request = urllib_request.Request(url=url, headers=headers)
    search_page = urllib_request.urlopen(search_request).read().decode('utf8')
    beautiful_soup_reset = BeautifulSoup(search_page, 'lxml')
    # print(beautiful_soup_reset)
    return beautiful_soup_reset


def get_news_count():
    # 获取新闻数字的变化
    data = get_search_data()
    # print(data)
    count_info = data.find('div', class_='listNum').text
    # print(count_info)
    # 1～20/233,270件 字符串操作 /^^^<
    return count_info[count_info.index('/') + 1:len(count_info) - 1]


def get_news():
    data = get_search_data()
    list_box_wrap = data.find_all('li', class_='ListBoxwrap')

    '''
    for i in list_box_wrap:
      print('news_title:', i.find(class_='title').find('dt').text)
      print('type:',list_box_wrap[0].find(class_='title').find('dd')[0].text)
       print('time:', i.find(class_='title').find('dd').find(class_='date').text)
      '''
    print('news_title:', list_box_wrap[0].find(class_='title').find('dt').text)

    print('time:', list_box_wrap[0].find(class_='title').find('dd').find(class_='date').text)

    print('img:', list_box_wrap[0].find(class_='thumb').find('img').get('data-src'))

    print('new_info:', list_box_wrap[0].find('a').get('href'))



    return 0
