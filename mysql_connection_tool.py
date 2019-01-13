import pymysql
from DBUtils.PooledDB import PooledDB
import config_reader as ini_r


class Mysql_Connection_Tool(object):
    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.connection = Mysql_Connection_Tool.get_mysql_connection()
        self.cursor_tool = self.connection.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    # db=ini_r.read_config('MysqlConfig', 'db')
    def get_mysql_connection():
        if Mysql_Connection_Tool.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20,
                              user=ini_r.read_config('MysqlConfig', 'user'),
                              passwd=ini_r.read_config('MysqlConfig', 'password'),
                              host=ini_r.read_config('MysqlConfig', 'host'),
                              # port is not str
                              db=ini_r.read_config('DataBase', 'db'),
                              port=int(ini_r.read_config('MysqlConfig', 'port')),
                              charset=ini_r.read_config('MysqlConfig', 'charset'))
            print('<database connection success!>')
        return __pool.connection()

    # 释放资源
    def disconnection(self):
        self.connection.close()
        self.cursor_tool.close()

    # 查找
    def search_database(self, sql):
        print('<search start>')
        self.cursor_tool.execute(sql)
        result = self.cursor_tool.fetchone()
        print('<search complete>')
        return result

    # 更新 增删改
    def update_database(self, sql):
        print('<update database>')
        insert_entity = self.cursor_tool.execute(sql)
        self.connection.commit()
        print('<update database success>')
        return insert_entity
