import fake_user
import mysql_connection_tool
import config_reader as ini_r
# fake_user.get_fake_user()
import yahoo_news_spider.data_repertory.yahoo_news_repertory as yns
import yahoo_news_spider.yahoo_news_search as ys

ys.get_news()


# print(ys.get_news_count())


#print(yns.create_table(table_name='demo5'))
#print(yns.drop_table(table_name='demo5'))
#print(yns.search_table(table_name='demo5'))
