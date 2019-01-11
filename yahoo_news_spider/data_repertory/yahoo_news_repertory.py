import mysql_connection_tool
import config_reader

database_link = mysql_connection_tool.Mysql_Connection_Tool()


# 创建数据库
def create_database(database_name):
    sql = 'CREATE DATABASE IF NOT EXISTS ' + database_name
    result = database_link.update_database(sql=sql)
    database_link.disconnection()
    '''
    if result > 0:
        config_reader.set_config('DataBase', 'db', database_name)
        return result
    else:
        print('<DATABASE CREATE FAILED>')
        return -1
    '''


def create_table(table_name):
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + '(Id INT PRIMARY KEY AUTO_INCREMENT,Title VARCHAR(100))'
    result = database_link.update_database(sql=sql)
    print(result)
    database_link.disconnection()
    return


# 删除数据库
def drop_database(database_name):
    return


# 添加数据
def insert_database(dict):
    return


def database_search(database_name):
    sql = "show databases like '{0}'".format(database_name)
    if database_link.search_database(sql=sql) is None:
        database_link.disconnection()
        return -1
    else:
        database_link.disconnection()
        return 0
