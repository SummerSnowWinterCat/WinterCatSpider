import fake_user
import mysql_connection_tool
# fake_user.get_fake_user()

import yahoo_news_spider.yahoo_news_search as ys

# ys.get_news_count()

database  = mysql_connection_tool.Mysql_Connection_Tool()

sql ='show tables'
res = database.search_database(sql)
print(res)



database.disconnection()