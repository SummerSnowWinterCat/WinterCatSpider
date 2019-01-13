import config_reader
import mysql_connection_tool

database_link = mysql_connection_tool.Mysql_Connection_Tool()


# 创建数据库
def create_database(database_name):
    if database_search(database_name) == -1:
        sql = 'CREATE DATABASE IF NOT EXISTS ' + database_name
        database_link.update_database(sql=sql)
        database_link.disconnection()
        config_reader.set_config('DataBase', 'db', database_name)
        print('database is created!')
    else:
        config_reader.set_config('DataBase', 'db', database_name)
        print('database create failed!')
        return -1


# 创建新闻表
def create_news_table(table_name):
    sql = 'CREATE TABLE IF NOT EXISTS ' \
          + table_name + \
          '(Id INT PRIMARY KEY AUTO_INCREMENT,' \
          'Title VARCHAR(100) NOT NULL,' \
          'News_Date DATETIME NOT NULL,' \
          'News_Info TEXT NOT NULL,' \
          'News_OverAll TEXT NOT NULL,' \
          'News_Img BLOB,' \
          'News_Link VARCHAR(150) NOT NULL,' \
          'News_Type TINYINT)'
    result = database_link.update_database(sql=sql)
    database_link.disconnection()
    print('<create news table success>')
    return result


# 查找表
def search_table(table_name):
    sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME ='{0}'".format(table_name)
    result = database_link.search_database(sql=sql)
    database_link.disconnection()
    return result


# 删除表
def drop_table(table_name):
    sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME ='{0}'".format(table_name)
    result = database_link.search_database(sql=sql)
    if result is None:
        print('<DROP TABLE FAILED> CODE:-1')
        database_link.disconnection()
        return -1
    else:
        sql = 'DROP TABLE ' + table_name
        result = database_link.update_database(sql=sql)
        print('<DROP TABLE SUCCESS!>')
        database_link.disconnection()
        return result


# 删除数据库
def drop_database(database_name):
    sql = 'DROP DATABASE ' + database_name
    result = database_link.update_database(sql=sql)
    database_link.disconnection()
    return result


# 添加数据
def insert_database(dict):
    return


# 查找数据库
def database_search(database_name):
    sql = "show databases like '{0}'".format(database_name)
    if database_link.search_database(sql=sql) is None:
        database_link.disconnection()
        return -1
    else:
        database_link.disconnection()
        return 0
