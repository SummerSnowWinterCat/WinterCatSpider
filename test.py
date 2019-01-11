import fake_user
import mysql_connection_tool
import config_reader as ini_r
# fake_user.get_fake_user()

import yahoo_news_spider.yahoo_news_search as ys

ys.get_news_info_data('https://news.yahoo.co.jp/pickup/6309848')