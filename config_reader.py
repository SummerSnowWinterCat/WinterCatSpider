import configparser


# 配置文件读取
def read_config(config_name, get_entity):
    config = configparser.ConfigParser()
    config.read('mysql_config.ini')
    return config.get(config_name, get_entity)
