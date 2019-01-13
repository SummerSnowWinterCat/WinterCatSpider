from bs4 import BeautifulSoup
import os
import urllib.request as urllib_request
import re
import ssl
import fake_user
import lxml
import sys

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
    # count_re=count_info[count_info.index('/') + 1:len(count_info) - 1]

    return count_info[count_info.index('/') + 1:len(count_info) - 1]


# 获取新闻的data return dict
def get_news_info_data(news_url):
    news_overall = ''
    news_info = {}
    headers = {'User-Agent': fake_user.get_fake_user()}
    search_request = urllib_request.Request(url=news_url, headers=headers)
    search_page = urllib_request.urlopen(search_request).read().decode('utf8')
    beautiful_soup_news = BeautifulSoup(search_page, 'lxml')
    # 获取新闻全部
    real_news_link = beautiful_soup_news.find('a', class_='newsLink').get('href')
    if real_news_link != '':
        headers = {'User-Agent': fake_user.get_fake_user()}
        search_request = urllib_request.Request(url=news_url, headers=headers)
        search_page = urllib_request.urlopen(search_request).read().decode('utf8')
        beautiful_soup_news = BeautifulSoup(search_page, 'lxml')
        # =  = = = = = =  = = = = = = == = = = = = = == = = =
        headers = {'User-Agent': fake_user.get_fake_user()}
        search_request = urllib_request.Request(url=beautiful_soup_news.find('a', class_='newsLink').get('href'),
                                                headers=headers)
        search_page = urllib_request.urlopen(search_request).read().decode('utf8')
        news_over_all_link = BeautifulSoup(search_page, 'lxml')
        # 段落一
        for i in news_over_all_link.findAll('p', class_='ynDetailText yjDirectSLinkTarget'):
            news_overall += i.text
        # print(news_overall)
        news_info.setdefault('news_overall', news_overall)
        # last time
        last_write = news_over_all_link.find('p', class_='ynCpName').text
        news_info.setdefault('last_write', last_write)
        #

        return news_info

    else:
        return -1


# 获取news
def get_news():
    news_title = ''
    news_time = ''
    img_info = ''
    news_info = ''
    news_link = ''
    data = get_search_data()
    list_box_wrap = data.find_all('li', class_='ListBoxwrap')
    '''
    for i in list_box_wrap:
      print('news_title:', i.find(class_='title').find('dt').text)
      print('type:',list_box_wrap[0].find(class_='title').find('dd')[0].text)
       print('time:', i.find(class_='title').find('dd').find(class_='date').text)
      '''

    news_title = list_box_wrap[0].find(class_='title').find('dt').text
    print(news_title)
    news_time = list_box_wrap[0].find(class_='title').find('dd').find(class_='date').text
    print(news_time)
    img_info = list_box_wrap[0].find(class_='thumb').find('img').get('data-src')
    print(img_info)
    news_link = list_box_wrap[0].find('a').get('href')
    print(get_news_info_data(news_link))

    return 0
